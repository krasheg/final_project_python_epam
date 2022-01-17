"""
Employee class used to represent employees
"""
from department_app import db


class Employee(db.Model):
    """
    Employee model, inherited from SQLAlchemy, describe our employee`s in our table

    """

    #: table name for instance of Employee
    __tablename__ = "employee"

    #: unique _id for each instance of Employee Model
    id = db.Column(db.Integer, primary_key=True)

    #: Employee`s name, cannot be empty
    name = db.Column(db.String(30), nullable=False)

    #: Employee`s date of birth, cannot be empty
    birth_date = db.Column(db.Date, nullable=False)

    #: department _id`s which employee belongs
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
        return {"_id": self.id, 'name': self.name, 'birth_date': self.birth_date.strftime("%m-%d-%Y"),
                'salary': self.salary,
                'department': {'name': self.department.name, "organisation": self.department.organisation}}

    def save_to_db(self):
        """
        saving changes to database
        """
        db.session.add(self)
        db.session.commit()
