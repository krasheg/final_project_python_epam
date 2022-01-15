#: This file consists of tests for employee api
from test_base import BaseTestCase
from datetime import date
from department_app.models.department import Department
from department_app.models.employee import Employee
from department_app import app
import json
import unittest
from http import HTTPStatus

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

if __name__ == '__main__':
    unittest.main()
