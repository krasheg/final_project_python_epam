import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
import logging.config
from config import Config
from department_app.views.index_view import index_bp
from department_app.views.department_view import departments_bp
from department_app.views.employee_view import employees_bp
from department_app.rest import department_api, employee_api

app = Flask(__name__)
# apply configuration
app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db, directory=Config.MIGRATION_DIR)

db.create_all()

app.register_blueprint(index_bp)
app.register_blueprint(employees_bp)
app.register_blueprint(departments_bp)

# api
api = Api(app)
# api for department
api.add_resource(department_api.DepartmentListApi, '/api/departments')
api.add_resource(department_api.DepartmentApi, '/api/departments/<id>')
# api for employee
api.add_resource(employee_api.EmployeeListApi, '/api/employees')
api.add_resource(employee_api.EmployeeApi, '/api/employees/<id>')
api.add_resource(employee_api.EmployeeSearchApi, '/api/employees/search')

# logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')

file_handler = logging.FileHandler(filename='app.log', mode='w')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger = app.logger
logger.handlers.clear()
app.logger.addHandler(file_handler)
app.logger.addHandler(console_handler)
app.logger.setLevel(logging.DEBUG)

werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.handlers.clear()
werkzeug_logger.addHandler(file_handler)
werkzeug_logger.addHandler(console_handler)
werkzeug_logger.setLevel(logging.DEBUG)
