"""file contains tests for employee views"""
import json
from http import HTTPStatus
from datetime import date
from department_app.tests.test_base import BaseTestCase
from department_app import app
from department_app.models.department import Department
from department_app.models.employee import Employee


class TestEmployeeView(BaseTestCase):
    """
    class with tests for employee views
    """

    def test_employees_page(self):
        """
        test for employees page
        """
        client = app.test_client()
        response = client.get("/employees/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_employee_page(self):
        """
        test for employee page
        """
        client = app.test_client()
        response = client.get("/employee/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_add_employee_view(self):
        """test for post method in employee view"""
        client = app.test_client()

        data = {
            "birth_date": "1990-10-28",
            "department": "Developer, Nvidia",
            "name": "Yehor Romaniuk",
            "salary": 1800
        }
        with self.assertRaises(ValueError):
            client.post('/employee/', data=data)
        department_1 = Department("Developer", "Nvidia")
        department_1.save_to_db()
        response = client.post('/employee/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_update_employee_page(self):
        """
        test for update employee page
        """
        department_1 = Department('Captains', 'Black Pearl')
        department_1.save_to_db()
        employee_1 = Employee('Jack Sparrow', date(1985, 5, 12), 2200, department_1)
        employee_1.save_to_db()
        client = app.test_client()
        response = client.get("/employees/1/update")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        data = {"uname": "New name",
                'ubirth_date': "1980-10-15",
                'usalary': 300,
                'udepartment': 'Captains, Black Pearl'}
        response = client.post("/employees/1/update", data=data)
        self.assertEqual(response.status_code,HTTPStatus.FOUND)


    def test_delete_employee_page(self):
        """
        test for deleting employees page
        """
        client = app.test_client()
        response = client.get("/employees/1/delete")
        self.assertEqual(response.status_code, HTTPStatus.OK)
