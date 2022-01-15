"""File contains tests for homepage view """

from http import HTTPStatus
from department_app import app
from department_app.tests.test_base import BaseTestCase


class TestIndexView(BaseTestCase):
    """
    Class for homepage view tests
    """

    def test_index(self):
        """
        test for homepage view
        """
        client = app.test_client()
        response_1 = client.get('/')
        response_2 = client.get('/index')
        self.assertEqual(response_1.status_code, HTTPStatus.OK)
        self.assertEqual(response_2.status_code, HTTPStatus.OK)
