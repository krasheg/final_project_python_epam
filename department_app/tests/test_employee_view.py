#: file contains tests for employee views

from test_base import BaseTestCase
from department_app import app
from http import HTTPStatus
from department_app.models.department import Department
from department_app.models.employee import Employee
from datetime import date
import unittest


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

    def test_delete_employee_page(self):
        """
        test for deleting employees page
        """
        client = app.test_client()
        response = client.get("/employees/1/delete")
        self.assertEqual(response.status_code, HTTPStatus.OK)
