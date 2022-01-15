"""
REST operations for working with employees
"""
from datetime import datetime
from flask import jsonify, request
from flask_restful import Resource

from department_app.service.employee_service import EmployeeService


def get_date_or_none(date_str, date_format='%m-%d-%Y'):
    """
    Returns date represented by date string and date format or None if date
    string has wrong type/doesn't match the format specified

    """
    try:
        return datetime.strptime(date_str, date_format).date()
    except (ValueError, TypeError):
        return None


class EmployeeSearchApi(Resource):
    """
    Class for searching employee by date of birth or by date period
    """

    @staticmethod
    def get():
        """

        finding employees by date of birth
        returns a list of employees in json
        """
        args = request.json
        date = get_date_or_none(args.get('date'))
        first_date = get_date_or_none(args.get('first_date'))
        last_date = get_date_or_none(args.get('last_date'))
        if date:
            employees = EmployeeService.get_employees_with_certain_birth_date(date)
            return jsonify([employee.json() for employee in employees])
        elif first_date and last_date:
            employees = EmployeeService.get_employees_born_in_period(first_date, last_date)
            return jsonify([employee.json() for employee in employees])
        else:
            return {"message": "Bad request"}, 400


class EmployeeListApi(Resource):
    """
    Class for defining employees list get/put requests

    """

    @staticmethod
    def get():
        """
        return  all employees in json format
        """
        return jsonify([employee.json() for employee in EmployeeService.get_employees()])

    @staticmethod
    def post():
        '''
        Add a new employee with request data

        return information about result

        '''
        employee_json = request.json
        if not employee_json:
            return {'message': 'Empty request'}, 400

        elif not employee_json.get('name') or not employee_json.get('birth_date') or not employee_json.get(
                'salary') or not \
                employee_json.get('department'):
            return {'message': 'Not enough information'}, 400

        try:
            EmployeeService.add_employee(employee_json)
        except ValueError:
            return {'message': 'Bad request, can`t add employee'}, 400
        return {'message': 'Employee has been successfully added'}, 201


class EmployeeApi(Resource):
    """
    Class defines get/put/update/delete methods for Employee

    """

    @staticmethod
    def get(_id):
        """

        return the employee with a given _id in json format

        """
        try:
            return jsonify(EmployeeService.get_employee_by_id(_id).json())
        except:
            return {'message': f'Couldn`t find employee by {_id=}'}, 404

    @staticmethod
    def put(_id):
        """
        update the employee with a given _id
        return: message with result
        """
        employee_json = request.json
        if not employee_json:
            return {'message': 'Empty request'}, 400
        try:
            EmployeeService.update_employee(_id, employee_json)
        except ValueError:
            return {'message': 'Bad request'}, 400
        return {"message": 'Employee has been successfully updated'}, 200

    @staticmethod
    def delete(_id):
        """
        Delete employee by his _id
        return result
        """
        try:
            EmployeeService.delete_employee(_id)
            return {"message": "Employee has been deleted"}, 200
        except ValueError:
            return {'message': 'Cannot delete employee'}, 404
