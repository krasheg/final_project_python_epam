"""
Employee service used to make database queries, this module defines the
following classes:

- `EmployeeService`, employee service
"""
from department_app import db
from department_app.models.employee import Employee
from department_app.service.department_service import DepartmentService
from sqlalchemy import and_
from datetime import datetime
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
            raise ValueError("No such employee in database")

    @staticmethod
    def add_employee(employee_json):
        """
        add a new employee to database
        :return: employee in json
        """
        try:
            name = employee_json['name']
            birth_date = datetime.strptime(employee_json['birth_date'], '%m-%d-%Y')
            salary = employee_json['salary']
            department_name = employee_json['department']['name']
            department_organisation = employee_json['department']['organisation']
        except:
            raise ValueError("Incorrect data")
        try:
            department = DepartmentService.get_department_by_name_and_organization(department_name,
                                                                                   department_organisation)
        except ValueError:
            raise KeyError("No such department")

        employee = Employee(name, birth_date, salary, department)
        employee.save_to_db()
        return employee.json()

    @classmethod
    def update_employee(cls, id, employee_json):
        """
        Updates employee data from json and his id
        :param id: id of employee for update
        :param employee_json: data for update
        :return: updated employee
        """
        employee = cls.get_employee_by_id(id)
        data = employee_json

        if not employee:
            raise ValueError(f"Could not find employee by {id=}")
        if data.get('name'):
            employee.name = data['name']
        if data.get('birth_date'):
            employee.birth_date = datetime.strptime(data['birth_date'], '%m-%d-%Y')
        if data.get('salary'):
            employee.salary = int(data['salary'])
        if data.get('department'):
            department = DepartmentService.get_department_by_name_and_organization(data['department']['name'],
                                                                                   data['department']['organisation'])
            employee.department = department
        try:

            employee.save_to_db()
            return employee
        except ValueError:
            return {'message': 'An error occurred while saving employee'}

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
