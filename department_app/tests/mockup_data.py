#: Data for using in test mocks

from datetime import date
from department_app.models.department import Department
from department_app.models.employee import Employee

department_1 = Department('Captains', 'Black Pearl')
department_2 = Department('Captains', 'Flying Dutchman')
department_3 = Department('Helpers', 'Black Pearl')

employee_1 = Employee('Jack Sparrow', date(1985, 5, 12), 2200, department_1)
employee_2 = Employee('Hector Barbossa', date(1956, 7, 10), 2100, department_1)
