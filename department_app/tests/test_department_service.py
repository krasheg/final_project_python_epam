#: file contains tests for departments services

from test_base import BaseTestCase
from department_app.models.department import Department
from department_app.models.employee import Employee
from department_app.service.department_service import DepartmentService
from datetime import date
import unittest


class TestDepartmentService(BaseTestCase):
    """
    class for department services tests
    """

    def test_get_all_departments(self):
        """
        test for service get_all_departments
        """
        department_1 = Department("Security", "Ajax")
        department_2 = Department("Oil and gas engineering", "Ukrtransgas")
        department_1.save_to_db()
        department_2.save_to_db()
        result = DepartmentService.get_all_departments()
        self.assertEqual(result, [department_1, department_2])

    def test_get_department_by_id(self):
        """
        test for service get_department_by_id
        """
        department_1 = Department("Security", "Ajax")
        department_1.save_to_db()  #: id == 1
        result = DepartmentService.get_department_by_id(1)
        self.assertEqual(1, result.id)
        #: check if not department
        with self.assertRaises(ValueError):
            DepartmentService.get_department_by_id(2)

    def test_get_department_by_name_and_organization(self):
        """
             test for service get_department_by_name_and_organization
             """
        department = Department("Test name", "Test Organization")
        department.save_to_db()
        self.assertEqual(
            DepartmentService.get_department_by_name_and_organization(department.name, department.organisation),
            department)
        #: check if wrong database
        with self.assertRaises(ValueError):
            DepartmentService.get_department_by_name_and_organization("Wrong name", department.organisation)

    def test_add_department(self):
        """
        test for service add_department
        """
        department = {
            'name': "Test Name",
            'organisation': "Test Organization"
        }
        DepartmentService.add_department(department)
        self.assertEqual(1, Department.query.count())
        # bad data
        department = {
            'anme': "Test Name",
            'organisation': "Test Organization"
        }
        with self.assertRaises(ValueError):
            DepartmentService.add_department(department)

    def test_update_department(self):
        """
        test for service update_department
        """
        department = Department("Test Name", "Test Organization")
        department.save_to_db()
        update_data = {"name": "New Name"}
        DepartmentService.update_department(1, update_data)
        department = DepartmentService.get_department_by_id(1)
        self.assertTrue("New Name", department.name)

        #: Bad data
        with self.assertRaises(ValueError):
            DepartmentService.update_department(2, update_data)

    def test_delete_department(self):
        """
        test for service delete_department
        """
        department = Department("Test Name", "Test Organization")
        department.save_to_db()
        self.assertEqual(1, Department.query.count())
        DepartmentService.delete_department(1)
        self.assertEqual(0, Department.query.count())
        # Bad data
        with self.assertRaises(ValueError):
            DepartmentService.delete_department(1)

    def test_calculate_average_salary(self):
        """
        test for service calculate_average_salary
        """
        department = Department("Test Department", "Test Organisation")
        employee_1 = Employee('Employee 1', date(1985, 5, 12), 5000, department)
        employee_2 = Employee('Employee 2', date(1977, 7, 12), 1000, department)
        department.save_to_db()
        employee_1.save_to_db()
        employee_2.save_to_db()
        DepartmentService.calc_avg_salary(DepartmentService.get_all_departments())
        self.assertEqual(3000, DepartmentService.get_department_by_id(1).average_salary)
        #: Bad data (employees salary)
        employee_3 = Employee('Employee 3', date(1977, 7, 12), "skhdv", department)
        employee_3.save_to_db()
        with self.assertRaises(ValueError):
            DepartmentService.calc_avg_salary(DepartmentService.get_all_departments())


if __name__ == '__main__':
    unittest.main()
