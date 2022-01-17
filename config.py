"""
file with configurations for sqlalchemy
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Base configuration
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'department_app/database/department_db.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MIGRATION_DIR = os.path.join('department_app', 'migrations')


class TestConfig(Config):
    """
    Test configuration

    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'department_app/tests/test.db')
