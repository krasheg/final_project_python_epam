"""
This module defines is used to populate database with departments and employees,
it defines the following:

Functions:

- `populate_database`: populate database with employees and departments
"""

from models.department import Department
from models.employee import Employee
from app import db
# db.create_all()


def populate_database():
    """
    Populate database with employees and departments

    :return: None
    """
    department_1 = Department('Research and Development', 'Google', 1000)
    department_2 = Department('Purchasing', 'Amazon', 2000)
    department_3 = Department('Human Resource Management', 'Huawei', 3000)

    db.session.add(department_1)
    db.session.add(department_2)
    db.session.add(department_3)


    employee_1 = Employee('John Doe', '02-12-1979', 2000, department_1)
    employee_2 = Employee('Jane Wilson', '14-05-1983', 2100, department_2)
    employee_3 = Employee('Will Hunting', '21-08-1988', 1800, department_3)


    db.session.add(employee_1)
    db.session.add(employee_2)
    db.session.add(employee_3)

    db.session.commit()
    db.session.close()

if __name__ == '__main__':

    populate_database()
    print("population succeed")
