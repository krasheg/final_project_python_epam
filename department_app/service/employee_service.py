"""
Employee service used to make database queries, this module defines the
following classes:

- `EmployeeService`, employee service
"""
from department_app import db
from department_app.models.employee import Employee
from sqlalchemy import and_
import json

class EmployeeService:
    """
    Employee service used to make database queries from employee table
    """

    @classmethod
    def get_employees(cls):
        """
        method return all employees from db
        :return: list of all employees
        """
        try:
            return db.session.query(Employee).all()
        except:
            return {"message": "Error while fetching employees"}

    @staticmethod
    def get_employee_by_id(employee_id):
        """
        method return employee with given id
        :param employee_id: id of employee
        :return: employee with given id
        """
        try:
            return db.session.query(Employee).filter_by(id=employee_id).first()
        except:
            return None

    @staticmethod
    def add_employee(employee_json):
        """
        add a new employee to database
        :param employee_json: dict with employee data
        :return: employee
        """
        data = json.loads(employee_json)
        try:
            employee = Employee(**data)
            db.session.add(employee)
            db.session.commit()
            return employee
        except:
            raise ValueError("Incorrect data")

    @classmethod
    def update_employee(cls, id, employee_json):
        """
        Updates employee data from json and his id
        :param id: id of employee for update
        :param employee_json: data for update
        :return: updated employee
        """
        employee = cls.get_employee_by_id(id)
        data = json.loads(employee_json)
        if not employee:
            raise ValueError(f"Could not find employee by {id=}")
        if data['name']:
            employee.name = data['name']
        if data['birth_date']:
            employee.birth_date = data['birth_date']
        if data['salary']:
            employee.birth_date = data['salary']
        if data['department']:
            employee.department = data['department']
        db.session.add(employee)
        db.session.commit()
        return employee

    @classmethod
    def delete_employee(cls, id):
        """
        delete employee from database by his id
        :param id: employee id
        """
        employee = cls.get_employee_by_id(id)
        if not employee:
            raise ValueError("Could not find employee")
        db.session.delete(employee)
        db.session.commit()

    @classmethod
    def get_employees_with_certain_birth_date(cls, birth_date):
        """
        return employees with certain birthdate

        :param birth_date: date of birth
        :return:employees that born on given date
        """
        employees = db.session.query(Employee).filter_by(birth_date=birth_date).all()

        return employees

    @staticmethod
    def get_employees_born_in_period(first_date, last_date):
        """
        Fetches employees born in given period from database
        :param first_date: date to fetch employees born after
        :param last_date: date to fetch employees born before
        :return: employees that born on given period
        """
        employees = db.session.query(Employee).filter(
            and_(
                Employee.birth_date >= first_date,
                Employee.birth_date < last_date
            )
        ).all()
        return employees
