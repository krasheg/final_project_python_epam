"""
This module defines is used to populate database with departments and employees.

Functions:

- `populate_database`: populate database with employees and departments
"""

from datetime import date
from department_app.models.department import Department
from department_app.models.employee import Employee
from department_app import db


def populate_database():
    """
    Populate database with employees and departments

    :return: None
    """
    department_1 = Department('Captains', 'Black Pearl')
    department_2 = Department('Captains', 'Flying Dutchman')
    department_3 = Department('Helpers', 'Black Pearl')

    db.session.add(department_1)
    db.session.add(department_2)
    db.session.add(department_3)

    employee_1 = Employee('Jack Sparrow', date(1985, 5, 12), 2200, department_1)
    employee_2 = Employee('Hector Barbossa', date(1956, 7, 10), 2100, department_1)
    employee_3 = Employee('Davy Jones', date(1971, 7, 10), 2100, department_2)
    employee_4 = Employee('Joshame Gibbs', date(1996, 9, 12), 1800, department_3)

    db.session.add(employee_1)
    db.session.add(employee_2)
    db.session.add(employee_3)
    db.session.add(employee_4)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    populate_database()
    print("population succeed")
