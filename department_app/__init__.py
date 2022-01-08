
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

###
from department_app.views.index_view import index_bp
from department_app.views.department_view import departments_bp
from department_app.views.employee_view import employees_bp


# db.create_all()
app.register_blueprint(index_bp)
app.register_blueprint(employees_bp)
app.register_blueprint(departments_bp)







if __name__ == '__main__':


    app.run(debug=True)
