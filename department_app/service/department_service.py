"""
Department service used to make database queries
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
        method return the department with given _id
        """
        department = db.session.query(Department).filter_by(id=department_id).first()
        if not department:
            raise ValueError('No department with _id ' + str(department_id))
        return department

    @staticmethod
    def get_department_by_name_and_organization(name, organisation):
        """
        method return the department with given name and organisation
        :return: department with the same name and organisation like in params
        """
        try:
            result = db.session.query(Department).filter_by(name=name, organisation=organisation).first()
            if not result:
                raise ValueError
            return result
        except Exception:
            raise ValueError("Department does not exist")

    @staticmethod
    def add_department(department_json):
        """
        method that adds a new department to the database
        :return: department
        """
        try:
            department = Department(department_json['name'], department_json['organisation'])
            department.save_to_db()
        except KeyError:
            raise ValueError("Can not add department")
        return department

    @classmethod
    def update_department(cls, department_id, department_json):
        """
        returns updated department
        """
        department = cls.get_department_by_id(department_id)
        if not department:
            raise ValueError('Invalid department _id')
        if department_json.get('name'):
            department.name = department_json['name']
        if department_json.get('organisation'):
            department.organisation = department_json['organisation']
        department.save_to_db()
        return department

    @classmethod
    def delete_department(cls, department_id):
        """
        delete department from department database by his _id
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
                except Exception:
                    raise ValueError("Employee`s salary cannot be zero")
                department.save_to_db()
        return departments
