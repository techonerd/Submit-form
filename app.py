from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy
from wtforms import TextField, SubmitField
app = Flask(__name__)
app.config['SECRET_KEY'] = 'GDtfDCFYjD'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db=SQLAlchemy(app)

class Example(db.Model):

    Student=db.Column('id', db.String,primary_key=True)
    Physics=db.column('data',db.String(120))
    Chemistry=db.column('data',db.String(120))
    Math=db.column('data',db.String(120))
class myForm(FlaskForm):
        Student = TextField("event")
        Physics = TextField("event")
        Chemistry = TextField("event")
        Math= TextField("event")
        submit = SubmitField("Enviar")
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)
