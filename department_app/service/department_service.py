"""
Department service used to make database queries, this module defines the
following classes:

- `DepartmentService`, department service
"""

from department_app import db
from department_app.models.department import Department


class DepartmentService:
    """
    Department service used to make database queries
    """

    @classmethod
    def get_all_departments(cls):
        """
        try to return all departments from database, if not- return an error

        :return: all departments
        """
        try:

            return db.session.query(Department).all()
        except:
            raise ValueError('An error occurred while returning all departments')

    @staticmethod
    def get_department_by_id(department_id):
        """
        method return the department with given id

        :param department_id: id of the searched department
        :return: department with id == department_id
        """
        department = db.session.query(Department).filter_by(id=department_id).first()
        if not department:
            raise ValueError('No department with id ' + department_id)
        return department

    @staticmethod
    def get_department_by_name_and_organization(name, organisation):
        """
        method return the department with given name and organisation

        :param name: name of the searched department
        :param organisation: organisation in which the department is
        :return: department with the same name and organisation like in params
        """
        try:
            return db.session.query(Department).filter_by(name=name, organisation=organisation).first()
        except:
            raise ValueError(f"Department with name {name} and organisation {organisation} does not exist")

    @staticmethod
    def add_department(department_json):
        """
        method that adds a new department to the database
        :param department_json: json with department name and organisation
        :return: department
        """
        try:
            department = Department(department_json['name'], department_json['organisation'])
            department.save_to_db()
        except:
            raise ValueError(f"Can not add department with name {department_json['name']} "
                             f"and organisation {department_json['organisation']}")
        return department

    @classmethod
    def update_department(cls, department_id, department_json):
        """
        returns updated department
        :param department_id: department`s id, which we will update
        :param department_json: json data for update
        :return: updated department
        """
        department = cls.get_department_by_id(department_id)
        if not department:
            raise ValueError('Invalid department id')
        if department_json.get('name'):
            department.name = department_json['name']
        if department_json.get('organisation'):
            department.organisation = department_json['organisation']
        department.save_to_db()
        return department

    @classmethod
    def delete_department(cls, department_id):
        """
        delete department from department database by his id
        :param department_id: id of department to delete
        :return: None
        """
        department = cls.get_department_by_id(department_id)
        if not department:
            raise ValueError('Cannot delete department')
        db.session.delete(department)
        db.session.commit()


    @staticmethod
    def calc_avg_salary(departments):
        """
        function that calculates the average salary for each department, save it in database  and returns it

        """
        for department in departments:
            if department.employees:
                try:
                    department.average_salary = int((sum([employee.salary for employee in department.employees])) / len(
                        department.employees))
                except ZeroDivisionError:
                    return "Employee`s salary cannot be zero"
                department.save_to_db()
        return departments
