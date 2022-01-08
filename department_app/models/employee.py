from department_app import db


# from department import Department

class Employee(db.Model):
    """
    Employee model, inherited from SQLAlchemy, describe our employee`s in our table

    """

    #: table name for instance of Employee
    __tablename__ = "employee"

    #: unique id for each instance of Employee Model
    id = db.Column(db.Integer, primary_key=True)

    #: Employee`s name, cannot be empty
    name = db.Column(db.String(30), nullable=False)

    #: Employee`s date of birth, cannot be empty
    birth_date = db.Column(db.Date, nullable=False)

    #: department id`s which employee belongs
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    #: employee`s salary
    salary = db.Column(db.Integer, nullable=False)

    def __init__(self, name, birth_date, salary, department):
        self.name = name
        self.birth_date = birth_date
        self.salary = salary
        self.department = department

    def json(self):
        """
        json representation of employee
        :return: dict
        """
        return {'name': self.name, 'birth_date': self.birth_date, 'salary': self.salary,
                'department': self.department}

    def save_to_db(self):
        """
        saving changes to database
        :return: None
        """
        db.session.add(self)
        db.session.commit()
    # def __repr__(self):
    #     """
    #     Returns string representation of employee
    #
    #     """
    #     return f'Employee({self.name}, {self.birth_date}, {self.salary})'
