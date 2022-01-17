"""file contains tests for department views"""
from http import HTTPStatus
import unittest
from department_app.tests.test_base import BaseTestCase
from department_app import app
from department_app.models.department import Department


class TestDepartmentView(BaseTestCase):
    """
    class for testing department views
    """

    def test_departments_page(self):
        """
        test for departments page
        """
        client = app.test_client()
        response = client.get('/departments')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_department_page(self):
        """
        test for department page
        """
        client = app.test_client()
        response = client.get('/department/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        data = {"name": "Test",
                "organisation": "Test Organization"}
        response = client.post('/department/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_update_department_page(self):
        """
        test for updating department page
        """
        client = app.test_client()
        response = client.get('/departments/1/update')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        department = Department("Created name", "Created organisation")
        department.save_to_db()
        response = client.get('/departments/1/update')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        data = {"uname": "Test",
                "uorganisation": "Test Organization"}
        response = client.post('/departments/1/update', data=data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        #: redirect if exist
        response = client.post('/departments/1/update', data=data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_delete_department_page(self):
        """
        test for deleting department page
        """
        client = app.test_client()
        department_1 = Department("Dep for delete", "Org for delete")
        department_1.save_to_db()
        response = client.get('/departments/1/delete')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(0, Department.query.count())


if __name__ == '__main__':
    unittest.main()
