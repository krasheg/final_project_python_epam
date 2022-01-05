
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

###



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/employees')
def employees():
    return render_template('employees.html')


@app.route('/departments')
def departments():
    return render_template('departments.html')






if __name__ == '__main__':


    app.run(debug=True)
