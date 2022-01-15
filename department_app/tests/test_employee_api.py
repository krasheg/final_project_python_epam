"""This file consists of tests for employee api"""
import json
import unittest
from http import HTTPStatus
from datetime import date
from department_app.tests.test_base import BaseTestCase
from department_app.models.department import Department
from department_app.models.employee import Employee
from department_app import app


class TestEmployeeApi(BaseTestCase):
    """
    Class for employee API tests
    """

    def test_employee_search_api(self):
        """
        test for searching employees in database by date birth or period
        """
        client = app.test_client()
        department = Department("Test name", "Test organisation")
        department.save_to_db()
        employee_1 = Employee('Jack Sparrow', date(1985, 5, 25), 2200, department)
        employee_1.save_to_db()
        employee_2 = Employee('Hector Barbossa', date(1956, 7, 12), 2100, department)
        employee_2.save_to_db()
        data = {"date": "05-25-1985"}
        response = client.get('/api/employees/search', data=json.dumps(data), content_type='application/json')
        self.assertEqual([employee_1.json()], response.json)
        period = {
            "first_date": "09-12-1950",
            "last_date": "12-12-1959"
        }
        response = client.get('/api/employees/search', data=json.dumps(period), content_type='application/json')
        self.assertEqual([employee_2.json()], response.json)
        #: Bad request.
        data = {"data": None}
        response = client.get('/api/employees/search', data=json.dumps(data), content_type='application/json')
        self.assertEqual({"message": "Bad request"}, response.json)
        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status_code)

    def test_get_all_employees(self):
        """
        test for get all employees
        """
        department_1 = Department('Captains', 'Black Pearl')
        department_1.save_to_db()
        employee_1 = Employee('Jack Sparrow', date(1985, 5, 12), 2200, department_1)
        employee_1.save_to_db()
        employee_2 = Employee('Hector Barbossa', date(1956, 7, 10), 2100, department_1)
        employee_2.save_to_db()
        client = app.test_client()
        response = client.get("/api/employees")
        self.assertEqual(response.json, [employee_1.json(), employee_2.json()])

    def test_post_employee(self):
        """
        test for posting new employee
        """
        department_1 = Department('Captains', 'Black Pearl')
        department_1.save_to_db()
        new_data = {
            "birth_date": "12-12-1992",
            "department": {
                "name": "Captains",
                "organisation": "Black Pearl"
            },
            "name": "Yehor Romaniuk",
            "salary": 1800
        }
        client = app.test_client()
        response = client.post("/api/employees", data=json.dumps(new_data), content_type='application/json')
        self.assertEqual({'message': 'Employee has been successfully added'}, response.json)
        #: Bad request.
        new_data['birth_date'] = "blablabla"
        response = client.post("/api/employees", data=json.dumps(new_data), content_type='application/json')
        self.assertEqual({'message': 'Bad request, can`t add employee'}, response.json)
        #: Not enough information
        new_data = {
            "birth_date": "12-12-1992",
            "name": "Yehor Romaniuk",
            "salary": 1800
        }
        response = client.post("/api/employees", data=json.dumps(new_data), content_type='application/json')
        self.assertEqual({'message': 'Not enough information'}, response.json)

    def test_get_employee_by_id(self):
        """
        test for getting employee by id
        """
        department_1 = Department('Engineering', 'Bethesda Softworks')
        department_1.save_to_db()
        employee_1 = Employee('Todd Howard', date(1985, 5, 12), 6000, department_1)
        employee_1.save_to_db()  #: id=1
        client = app.test_client()
        response = client.get("/api/employees/1", )
        self.assertEqual(employee_1.json(), response.json)
        #: Bad request
        response = client.get("/api/employees/2", )
        self.assertEqual({'message': "Couldn`t find employee by id='2'"}, response.json)

    def test_put_employee(self):
        """
        test for replace employee with new data
        """
        department_1 = Department('Engineering', 'Bethesda Softworks')
        department_1.save_to_db()
        employee_1 = Employee('Todd Howard', date(1985, 5, 12), 6000, department_1)
        employee_1.save_to_db()
        new_data = {
            'name': "Ashley Cheng Craig Lafferty"
        }
        client = app.test_client()
        response = client.put("/api/employees/1", data=json.dumps(new_data), content_type='application/json')
        self.assertEqual({"message": 'Employee has been successfully updated'}, response.json)
        #: Empty request
        response = client.put("/api/employees/1", data=json.dumps(None), content_type='application/json')
        self.assertEqual({'message': 'Empty request'}, response.json)
        #: Bad Request
        new_data = {
            'surname': "Ashley Cheng Craig Lafferty"
        }
        response = client.put("/api/employees/1", data=json.dumps(new_data), content_type='application/json')
        self.assertEqual({'message': 'Bad request'}, response.json)

    def test_delete_employee(self):
        department_1 = Department('Engineering', 'Bethesda Softworks')
        department_1.save_to_db()
        employee_1 = Employee('Todd Howard', date(1985, 5, 12), 6000, department_1)
        employee_1.save_to_db()
        client = app.test_client()
        response = client.delete("/api/employees/1")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json, {"message": "Employee has been deleted"})

        #: Call error
        response = client.delete("/api/employees/3")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        self.assertEqual(response.json, {'message': 'Cannot delete employee'})


if __name__ == '__main__':
    unittest.main()
