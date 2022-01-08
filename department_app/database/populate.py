"""
This module defines is used to populate database with departments and employees,
it defines the following:

Functions:

- `populate_database`: populate database with employees and departments
"""

from datetime import date
from department_app.models.department import Department
from department_app.models.employee import Employee
from department_app import db
db.create_all()


def populate_database():
    """
    Populate database with employees and departments

    :return: None
    """
    department_1 = Department('Research and Development', 'Google')
    department_2 = Department('Purchasing', 'Amazon')
    department_3 = Department('Human Resource Management', 'Huawei')

    db.session.add(department_1)
    db.session.add(department_2)
    db.session.add(department_3)


    employee_1 = Employee('John Doe', date(1985, 5, 12), 2000, department_1)
    employee_2 = Employee('Jane Wilson', date(1971, 7, 10), 2100, department_2)
    employee_3 = Employee('Will Hunting', date(1996, 9, 12), 1800, department_3)


    db.session.add(employee_1)
    db.session.add(employee_2)
    db.session.add(employee_3)

    db.session.commit()
    db.session.close()

if __name__ == '__main__':

    populate_database()
    print("population succeed")
