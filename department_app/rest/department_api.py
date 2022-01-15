"""
REST operations for working with departments
"""
from flask import jsonify, request
from flask_restful import Resource
from department_app.models.department import Department
from department_app.service.department_service import DepartmentService


class DepartmentListApi(Resource):
    """
    Class for defining department`s list get/put requests

    """

    @staticmethod
    def get():
        """
        return  all departments in json format
        """
        DepartmentService.calc_avg_salary(Department.query.all())
        return jsonify([department.json() for department in DepartmentService.get_all_departments()])

    @staticmethod
    def post():
        '''
        Add a new department with request data

        return information about result

        '''
        department_json = request.json
        if not department_json:
            return {'message': 'Empty request'}, 400

        elif not department_json.get('name') or not department_json.get('organisation'):
            return {'message': 'Bad request'}, 400

        try:
            DepartmentService.add_department(department_json)
        except ValueError:
            return {'message': 'Bad request'}, 400
        return {'message': 'Department has been successfully added'}, 201


class DepartmentApi(Resource):
    """
    Class defines get/put/patch/delete methods for Department

    """

    @staticmethod
    def get(id):
        """

        return the department with a given id in json format

        """
        DepartmentService.calc_avg_salary(Department.query.all())
        department = DepartmentService.get_department_by_id(id).json()
        return department, 200

    @staticmethod
    def put(id):
        """
        partially updates the existing department
        return: message with result
        """
        department_json = request.json
        if not department_json:
            return {'message': 'Empty request'}, 400
        try:
            DepartmentService.update_department(id, department_json)
        except ValueError:
            return {'message': 'Bad request'}, 400
        return {"message": 'Department has been successfully updated'}, 200

    @staticmethod
    def delete(id):
        """
        Delete department
        return result
        """
        try:
            DepartmentService.delete_department(id)
            return {"message": "Department has been deleted"}, 200
        except ValueError:
            return {'message': 'Cannot delete department'}, 404
