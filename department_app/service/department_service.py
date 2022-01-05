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
            return {'message': 'An error occurred while returning all departments'}

    @staticmethod
    def get_department_by_id(department_id):
        """
        method return the department with given id

        :param department_id: id of the searched department
        :return: department with id == department_id
        """
        department = db.session.query(Department).filter_by(id=department_id).first()
        if not department:
            return {'message': 'No department with id ' + department_id}
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
            return db.session.query(Department).filter_by(name=name, organisation=organisation)
        except:
            return {"message": f"Department with name {name} and organisation {organisation} does not exist"}

    @staticmethod
    def add_department(department_json):
        pass

    @staticmethod
    def update_department(id,department_json):
        pass

    @staticmethod
    def calc_avg_salary(department):
        """
        переделать!!!
        для каждого департмент айди найти всех работников, сделать список с зарплат, взять сумму и поделить на длину
         списка во флоте. записать в бд
        :param department:
        :return:
        """
        try:
            department.average_salary = (sum([employee.salary for employee in department.employees])) / len(
                department.employees)
            return department
        except ZeroDivisionError:
            return department


