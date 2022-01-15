#: This file consists of tests for employee services

from test_base import BaseTestCase
from department_app import app
from department_app.models.department import Department
from department_app.models.employee import Employee
from department_app.service.employee_service import EmployeeService
from datetime import date
import unittest


class TestEmployeeService(BaseTestCase):
    """
    class for testing employee service.
    """

    def test_get_all_employees(self):
        """
        test for get employees service
        """
        client = app.test_client()
        department = Department("Test name", "Test organisation")
        department.save_to_db()
        employee_1 = Employee('Jack Sparrow', date(1985, 5, 25), 2200, department)
        employee_1.save_to_db()
        employee_2 = Employee('Hector Barbossa', date(1956, 7, 12), 2100, department)
        employee_2.save_to_db()
        result = EmployeeService.get_employees()
        self.assertEqual(result, [employee_1, employee_2])

    def test_get_employee_by_id(self):
        """
        test for getting employee by id
        """
        department = Department("Test name", "Test organisation")
        department.save_to_db()
        employee_1 = Employee('Test employee', date(1985, 5, 25), 2200, department)
        employee_1.save_to_db()  #: id =1
        result = EmployeeService.get_employee_by_id(1)
        self.assertEqual(1, result.id)
        #: check if not department
        with self.assertRaises(ValueError):
            EmployeeService.get_employee_by_id(2)

    def test_add_employee(self):
        """
        test for add employee service
        """
        department = Department("Test name", "Test organisation")
        department.save_to_db()
        data = {
            "birth_date": "12-12-1992",
            "department": {
                "name": "Test name",
                "organisation": "Test organisation"
            },
            "name": "Yehor Romaniuk",
            "salary": 1800
        }
        EmployeeService.add_employee(data)
        self.assertEqual(1, Employee.query.count())
        #: bad data
        employee = {
            "birth_date": "123-12-1992",
            "department": {
                "name": "Test name",
                "organisation": "Test organisation"
            },
            "name": "Yehor Romaniuk",
            "salary": 1800
        }
        with self.assertRaises(ValueError):
            EmployeeService.add_employee(employee)
        #: NO such department
        employee = {
            "birth_date": "12-12-1992",
            "department": {
                "name": "NO name",
                "organisation": "NO organisation"
            },
            "name": "Yehor Romaniuk",
            "salary": 1800
        }
        with self.assertRaises(KeyError):
            EmployeeService.add_employee(employee)

    def test_update_employee(self):
        """
        test for updating employee
        """
        department = Department("Test name", "Test organisation")
        department.save_to_db()
        employee_1 = Employee('Test employee', date(1985, 5, 25), 2200, department)
        employee_1.save_to_db()  #: id =1
        new_data = {
            'name': "New name"
        }
        EmployeeService.update_employee(1, new_data)
        employee = EmployeeService.get_employee_by_id(1)
        self.assertEqual("New name", employee.name)
        #: no such employee
        with self.assertRaises(ValueError):
            EmployeeService.update_employee(2, new_data)

    def test_delete_employee(self):
        department = Department("department", "Test organisation")
        department.save_to_db()
        employee_1 = Employee('Test employee', date(1985, 5, 25), 2200, department)
        employee_1.save_to_db()  #: id =1
        EmployeeService.delete_employee(1)
        self.assertEqual(0, Employee.query.count())
        #: bad id
        with self.assertRaises(ValueError):
            EmployeeService.delete_employee(1)

    def test_get_employees_with_certain_birth_date(self):
        """
        test for searching employee by date of birth
        """
        department = Department("New department", "Test organisation")
        department.save_to_db()
        employee_1 = Employee('Jack Sparrow', date(1985, 5, 25), 2200, department)
        employee_1.save_to_db()
        employee_2 = Employee('Hector Barbossa', date(1956, 7, 12), 2100, department)
        employee_2.save_to_db()
        self.assertEqual(EmployeeService.get_employees_with_certain_birth_date(date(1985, 5, 25)), [employee_1])

    def test_get_employees_born_in_period(self):
        """
        test for searching by date of birth in period
        """
        department = Department("test", "Test organisation")
        department.save_to_db()
        employee_1 = Employee('Jack Sparrow', date(1985, 5, 25), 2200, department)
        employee_1.save_to_db()
        employee_2 = Employee('Hector Barbossa', date(1956, 7, 12), 2100, department)
        employee_2.save_to_db()
        employee_3 = Employee('Davy Jones', date(1971, 7, 10), 2100, department)
        employee_3.save_to_db()
        self.assertEqual(EmployeeService.get_employees_born_in_period(date(1956, 5, 2), date(1972, 7, 10)),
                         [employee_2, employee_3])


if __name__ == '__main__':
    unittest.main()
