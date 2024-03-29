""" Views for manage employees on web application"""

from datetime import datetime
from flask import Blueprint, render_template, request, redirect
from department_app.models.employee import Employee
from department_app.models.department import Department
from department_app.service.employee_service import EmployeeService
from department_app.service.department_service import DepartmentService

employees_bp = Blueprint('employees_bp', __name__, template_folder='templates')


@employees_bp.route('/employee/', methods=['GET', 'POST'])
def add_employee():
    """
    Show user the page which allows manage employees (add, edit, delete)
    Collect employee's input data from forms and add it to database
    """
    departments = Department.query.all()
    employees = Employee.query.all()

    if request.method == 'POST':
        name = request.form['name']
        birth_date = datetime.strptime(request.form['birth_date'], '%Y-%m-%d')
        salary = request.form['salary']
        department_name = request.form['department'].split(', ')[0]
        department_organisation = request.form['department'].split(', ')[1]
        #: check if there is unique employee
        for employee in employees:
            if employee.name == name and employee.birth_date == birth_date:
                return redirect('/employees/')
        department = DepartmentService.get_department_by_name_and_organization(department_name, department_organisation)
        employee = Employee(name, birth_date, salary, department)
        employee.save_to_db()
        return redirect('/employees/')
    return render_template('employee.html', departments=departments, employees=employees)


@employees_bp.route("/employees/<int:_id>/update", methods=["GET", "POST"])
def update_employee(_id):
    """
    function for updating employee`s data
    """
    #: find employee by his _id
    employee = Employee.query.get(_id)
    #: all departments in database
    departments = Department.query.all()
    if request.method == 'POST':
        name = request.form['uname']
        birth_date = datetime.strptime(request.form['ubirth_date'], '%Y-%m-%d')
        salary = request.form['usalary']
        department = request.form.get('udepartment')
        #: apply only non-empty data
        if name:
            employee.name = name
        if birth_date:
            employee.birth_date = birth_date
        if salary:
            employee.salary = salary
        if department is not None:
            department_name = department.split(', ')[0]
            department_organisation = department.split(', ')[1]
            department = DepartmentService.get_department_by_name_and_organization(department_name,
                                                                                   department_organisation)
            employee.department = department
        employee.save_to_db()
        return redirect('/employees/')
    return render_template('employee.html', employee=employee, departments=departments)


@employees_bp.route("/employees/<int:_id>/delete")
def delete_employee(_id):
    """
    function for deleting employee by his id
    """
    EmployeeService.delete_employee(_id)
    return redirect('/employees/')


@employees_bp.route('/employees/')
def show_employees():
    """
    Show all employees from database
    """
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)


@employees_bp.route('/employees/search_by_date/', methods=['GET', 'POST'])
def show_employees_by_date():
    """
    Show all employees born in definite date
    """
    if request.method == 'POST':
        date = request.form['date']
        employees = EmployeeService.get_employees_with_certain_birth_date(date)
        return render_template('employees.html', employees=employees)


@employees_bp.route('/employees/search_by_period/', methods=['GET', 'POST'])
def show_employees_by_period():
    """
    Show all employees born in definite period
    """
    if request.method == 'POST':
        first_date = request.form['first_date']
        last_date = request.form['last_date']
        employees = EmployeeService.get_employees_born_in_period(first_date, last_date)
        return render_template('employees.html', employees=employees)

