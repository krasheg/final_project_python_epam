from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

from config import Config

app = Flask(__name__)
# apply configuration
app.config.from_object(Config)
db = SQLAlchemy(app)


migrate = Migrate(app, db, directory=Config.MIGRATION_DIR)

from department_app.views.index_view import index_bp
from department_app.views.department_view import departments_bp
from department_app.views.employee_view import employees_bp

db.create_all()

app.register_blueprint(index_bp)
app.register_blueprint(employees_bp)
app.register_blueprint(departments_bp)

from department_app.rest import department_api, employee_api

# api
api = Api(app)
# api for department
api.add_resource(department_api.DepartmentListApi, '/api/departments')
api.add_resource(department_api.DepartmentApi, '/api/departments/<id>')
# api for employee
api.add_resource(employee_api.EmployeeListApi, '/api/employees')
api.add_resource(employee_api.EmployeeApi, '/api/employees/<id>')
api.add_resource(employee_api.EmployeeSearchApi, '/api/employees/search')
