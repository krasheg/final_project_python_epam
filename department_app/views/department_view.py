# Department view for respond to requests to application.


from flask import Blueprint, render_template, request, redirect,url_for
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
        department = None
        form = request.form
        name = form['name']
        organisation = form['organisation']
        if DepartmentService.get_department_by_name_and_organization(name, organisation):
            return redirect('/departments')
        try:
            department = Department(name, organisation)
            department.save_to_db()
            return redirect('/departments')
        except:
            return "An error occurred while saving the department"
    departments = Department.query.all()
    return render_template('department.html', departments=departments)


@departments_bp.route("/departments/<int:id>/update", methods=['POST', 'GET'])
def update_department(id):
    """
    update department from database id with form data
    """
    department = Department.query.get(id)
    if request.method == 'POST':
        name = request.form['uname']
        if name:
            department.name = name

        organisation = request.form['uorganisation']
        if organisation:
            department.organisation = organisation

        try:
            db.session.commit()
            return redirect("/departments")
        except:
            return "An error occured while updating department"
    return render_template('department.html', department=department)


@departments_bp.route("/departments/<int:id>/delete")
def delete_department(id):
    """
    deletes department from db by his id
    """
    department = Department.query.get(id)
    try:
        db.session.delete(department)
        db.session.commit()
        return redirect("/departments")
    except:
        return "An error occured while deleting department"



@departments_bp.route("/departments")
def show_departments():
    """
    show all departments in database and calculate department`s average salary
    """
    departments = DepartmentService.calc_avg_salary(Department.query.all())
    return render_template("departments.html", departments=departments)
