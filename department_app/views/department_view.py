"""Department views used to manage departments on web application"""

from flask import Blueprint, render_template, request, redirect
from department_app import db
from department_app.models.department import Department
from department_app.service.department_service import DepartmentService

departments_bp = Blueprint('departments_bp', __name__, template_folder='templates')


@departments_bp.route('/department/', methods=['GET', 'POST'])
def add_department():
    """
    Show user the page which allows manage departments (add, edit, delete)
    Collect department's input data from forms and add it to database
    """
    if request.method == 'POST':
        form = request.form
        name = form['name']
        organisation = form['organisation']
        try:
            if DepartmentService.get_department_by_name_and_organization(name, organisation):
                return redirect('/departments')
        except ValueError:
            department = Department(name, organisation)
            department.save_to_db()
            return redirect('/departments')
    departments = Department.query.all()
    return render_template('department.html', departments=departments)


@departments_bp.route("/departments/<int:_id>/update", methods=['POST', 'GET'])
def update_department(_id):
    """
    update department from database _id with form data
    """
    department = Department.query.get(_id)
    if request.method == 'POST':
        name = request.form['uname']
        if name:
            department.name = name

        organisation = request.form['uorganisation']
        if organisation:
            department.organisation = organisation
        db.session.commit()
        return redirect("/departments")
    return render_template('department.html', department=department)


@departments_bp.route("/departments/<int:_id>/delete")
def delete_department(_id):
    """
    deletes department from db by his _id
    """
    department = Department.query.get(_id)
    db.session.delete(department)
    db.session.commit()
    return redirect("/departments")



@departments_bp.route("/departments")
def show_departments():
    """
    show all departments in database and calculate department`s average salary
    """
    departments = DepartmentService.calc_avg_salary(Department.query.all())
    return render_template("departments.html", departments=departments)
