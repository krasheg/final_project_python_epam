from department_app import db


class Department(db.Model):
    """
        Department model, inherited from SQLAlchemy, describe our departments in our table

        """

    #: table name for instance of Department_model
    __tablename__ = "department"

    #: unique id for each instance of Department Model
    id = db.Column(db.Integer, primary_key=True)

    #: Department`s name, cannot be empty
    name = db.Column(db.String(30), nullable=False)

    #: department`s organisation name, cannot be empty
    organisation = db.Column(db.String(30), nullable=False)

    #: department id`s which employee belongs
    employees = db.relationship("Employee", backref=db.backref('department'))


    def __init__(self, name, organisation, employees=None):
        self.name = name
        self.organisation = organisation
        self.average_salary = 0
        if not employees:
            employees = []
        #: Employees that working in the department
        self.employees = employees

