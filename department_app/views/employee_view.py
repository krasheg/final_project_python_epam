#: Views for manage employees on web application,


from flask import Blueprint, render_template, request, redirect
from datetime import date, datetime
from department_app import db
from department_app.models.employee import Employee
from department_app.models.department import Department

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
        update = False  # marker for form
        name = request.form['name']
        birth_date = datetime.strptime(request.form['birth_date'], '%Y-%m-%d')
        salary = request.form['salary']
        department = request.form['department']
        #: check if there is unique employee
        for employee in employees:
            if employee.name == name and employee.birth_date == birth_date:
                return redirect('/employees/')
        for dep in departments:
            if dep.name == department:
                department = dep
                break
        else:
            return "No such department"
        employee = Employee(name, birth_date, salary, department)
        try:
            employee.save_to_db()
            return redirect('/employees/')
        except:
            return "An error occurred while saving to database database"
    return render_template('employee.html', departments=departments, employees=employees)


@employees_bp.route("/employees/<int:id>/update", methods=["GET", "POST"])
def update_employee(id):
    """
    function for updating employee`s data

    """
    #: marker for form
    update = True
    #: find employee by his id
    employee = Employee.query.get(id)
    #: all departments in database
    departments = Department.query.all()
    if request.method == 'POST':
        name = request.form['uname']
        birth_date = datetime.strptime(request.form['ubirth_date'], '%Y-%m-%d')
        salary = request.form['usalary']
        department = request.form['udepartment']
        #: apply only non-empty data
        if name:
            employee.name = name
        if birth_date:
            employee.birth_date = birth_date
        if salary:
            employee.salary = salary
        if department:
            #: swap department name from form to his id in database
            for dep in departments:
                if dep.name == department:
                    department = dep
                    break
            else:
                return "No such department"
            employee.department = department

            try:
                db.session.commit()
                return redirect('/employees/')
            except:
                return "An error occurred while saving employee`s data"
    return render_template('employee.html', employee=employee, update=update, departments=departments)

@employees_bp.route("/employees/<int:id>/delete")
def delete_employee(id):
    employee = Employee.query.get(id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return redirect('/employees/')
    return "An error occurred while deleting employee"


@employees_bp.route('/employees/')
def show_employees():
    """
    Show all employees from database
    """
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)
