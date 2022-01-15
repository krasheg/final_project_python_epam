#: file contains tests for department views

from test_base import BaseTestCase
from department_app import app
from http import HTTPStatus
import unittest


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

    def test_update_department_page(self):
        """
        test for updating department page
        """
        client = app.test_client()
        response = client.get('/departments/1/update')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_delete_department_page(self):
        """
        test for deleting department page
        """
        client = app.test_client()
        response = client.get('/departments/1/delete')
        self.assertEqual(response.status_code, HTTPStatus.OK)



if __name__ == '__main__':
    unittest.main()
