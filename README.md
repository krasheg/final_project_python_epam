[![Coverage Status](https://coveralls.io/repos/github/krasheg/final_project_python_epam/badge.svg?branch=main)](https://coveralls.io/github/krasheg/final_project_python_epam?branch=main)

# Department App

***
Department App is web application for managing departments and employees within organisations. It uses RESTful web
service to perform CRUD operations. The user is allowed to:

***

## How to start

__Project uses python v.3.9__

***

## How to deploy

### Clone the _repo_:

> `git clone https://github.com/krasheg/final_project_python_epam`

### Create the virtual environment in project and activate it:

> `cd epam_winter2021_project-main`

> `python -m venv env`

> `source venv/bin/activate` On linux

> `cd venv/Scripts/activate` On Windows

### How to install project packages:

> `pip install -r requirements.txt`

### How to run the migration scripts to create database schema:

> `flask db init` - further use is optional, in case of intentional reinstallation

> `flask db migrate`

> `flask db update`
***

##### After these steps you can see the index page of the application:

`localhost:5000/`

or

`localhost:5000/index`

***

# API operations

> `localhost:5000/api/departments`

* GET - show all departments

* POST - add new department with data:

`{'name': 'department name', 'organisation': 'department organisation'}`


> `localhost:5000/api/department/<id>`

* GET - show department by id
* PUT - update department by given data:

  `{'name': 'Department name' }`
  or
  `{'organisation': 'Department organisation' }`
* DELETE - delete department by given id

> `localhost:5000/api/employees`

* GET - show all employees
* POST - add new employee with given data:
  `{
  "birth_date": "MM-DD-YYY", "department": {
  "name": " Department name",
  "organisation": "Department organisation"
  },
  "name": "Employee name",
  "salary": int(salary)
  }`

> `localhost:5000/api/employee/<id>`

* GET - show employee by id
* PUT - update employee by id with data:
  `{
  "birth_date": "MM-DD-YYY", "department": {
  "name": " Department name",
  "organisation": "Department organisation"
  },
  "name": "Employee name",
  "salary": int(salary)
  }` (one of the field is required)

> `localhost:5000/api/employees/search`

* GET - show employees by birth date if `{
  "date": "MM-DD-YYY"
  }` or show employees born in period if `{
  "first_date": "MM-DD-YYY",
  "last_date": "MM-DD-YYY"
  }`





