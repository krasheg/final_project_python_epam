"""
This module has base test class for inherit configuration with setup
"""
import unittest
from config import TestConfig
from department_app import app, db


class BaseTestCase(unittest.TestCase):
    """
    Base test class for inherited tests
    """

    def setUp(self):
        self.app = app
        self.app.config.from_object(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        #: removing temporary database
        db.session.remove()
        db.drop_all()
