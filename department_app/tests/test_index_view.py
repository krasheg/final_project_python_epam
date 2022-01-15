#: File contains tests for homepage view
import http

from department_app import app
from test_base import BaseTestCase
from http import HTTPStatus


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
