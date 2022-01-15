# Department App

***
Department App is a web application that provides information about departments and employees

The application should provide such functionality:

1. Adding and storing departments and employees in the database

2. Display the lists of departments and employees

3. Ability to add, edit and delete departments and employees

4. Display the number, average salary (calculated automatically based on the employees' salaries) of employees for each
   department

5. Ability to assign an employee to the department
6. Search employee by date of birth or period

***

### Home page

When the user enters the home page, they see a large heading and a short description of what this application can do.

#### Main scenario:

User opens a site and see the home page

![alt text](screenshots/homepage.png)

Pic. 1 The home page

***

### Departments

Display the list of departments

#### Main scenario:

User clicks the 'Departments' which redirects them to the departments page where they can see the following:

1. Department (name of the department)

2. Organisation

3. Employee Count

4. Average Salary (average salary of all employees in department)

5. Update (when clicked redirects to the edit departments page where user can edit current department)

6. Delete (Delete a department without any redirects)

![alt text](screenshots/departments.png)

Pic. 2 The list of departments
***

### Manage departments

Display departments managing page

#### Main scenario:

User clicks the 'Department' button on the home page and pushes the button "update"
opposite the desired department which redirects them to the department update page where they can change information
about department.

![alt text](screenshots/update_department.png)

Pic. 3.1 Update department page
***
Also user can click on "delete" button opposite chosen department to delete it.

![alt text](screenshots/delete_department.png)

Pic. 3.2 Delete departments
***

In the very bottom of the departments page user can click "add department" button which redirects them to the department
creation page were he can create a new department

![alt text](screenshots/add_new_department.png)

Pic. 3.3 Add department page
***

### Employees

Display the list of employees

#### Main scenario:

User clicks the 'Employees' button which redirects them to the employees page where they can see the following:

1. Employee (name of the employee)

2. Employee date of birth

3. Salary

4. Department (to which the employee belongs)

5. Update button (when clicked redirects to the manage employee page where user can change info about employee)

6. Delete button (delete an employee )

![alt text](screenshots/employees.png)

Pic. 4 The list of employees
***

### Manage employees

Display employee managing page

#### Main scenario:

User clicks the 'Employees' button on the home page and push 'update' button opposite chosen employee which redirects
them to the employees manage page where they can change the information about chosen employee.

![alt text](screenshots/update_employee.png)

Pic. 4.1 Update employee page
***
Also user can click on "delete" button opposite chosen department to delete it.

![alt text](screenshots/delete_employee.png)

Pic. 4.2 Delete employee
***
In the very bottom of the employees page user can click "add employee" button which redirects them to the employee
creation page were he can create a new employee

![alt text](screenshots/add_new_employee.png)

Pic. 4.2 Add employees
***

### Search

Display the list of employees that born in a chosen date or period

#### Main scenario:

User clicks the 'Search by date' dropdown menu and choose date or date period which redirects them to the page with employees
that born in searched date or period

![alt text](screenshots/employees_search.png)
Pic. 5 Search employees
***
