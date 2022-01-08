from department_app import create_app
#from department_app.database import populate

app = create_app()
if __name__ == '__main__':
    # populate.populate_database()
    app.run(debug=True)