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


    #: Employees that working in the department
    employees = db.relationship(
        'Employee',
        cascade="all,delete",
        backref=db.backref('department', lazy=True),
        lazy=True
    )





    def __init__(self, name, organisation):
        self.name = name
        self.organisation = organisation
        self.average_salary = 0

    def json(self):
        """
        json representation of department
        :return: dict
        """
        return {'name': self.name, 'organisation': self.organisation, 'average_salary': self.average_salary}


    def save_to_db(self):
        """
        saving changes to database
        :return: None
        """
        db.session.add(self)
        db.session.commit()

    # def __repr__(self):
    #     """
    #     Returns string representation of department
    #
    #     """
    #     return f'Employee({self.name}, {self.organisation}, {self.employees})'
