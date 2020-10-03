from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
# from flask_wtf.csrf import CSRFProtect, CSRFError
# from wtforms import DateField, StringField, TextAreaField
from wtforms.validators import DataRequired
# from wtforms_components import TimeField
from flask_sqlalchemy import SQLAlchemy
# from flask.ext.wtf import Form
from wtforms import TextField, SubmitField
app = Flask(__name__)
app.config['SECRET_KEY'] = 'GDtfDCFYjD'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db=SQLAlchemy(app)
# csrf = CSRFProtect()
# csrf.init_app(app)
class Example(db.Model):
    # __tablename__='example'
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
#         # endDay = DateField("endDay", validators=[DataRequired()])
#         # endTime = TimeField("endTime", validators=[DataRequired()])
#         # details = TextAreaField("details", validators=[DataRequired()])
# # @app.route('/')
# # def index():
# #     return render_template('index.html')
@app.route('/')
def index():
    # colours = ['Red', 'Blue', 'Black', 'Orange']
    return render_template('index.html')
    # form = myForm()
    # if form.validate_on_submit():
    #     # global count
    #     # count += 1
    #     # putData = {'Event': form.event.data, 'Location': form.location.data, 'startDay': form.startDay.data, 'startTime': form.startTime.data,'endDay': form.endDay.data, 'endTime': form.endTime.data, 'Details': form.details.data}
    #     # firebase.put('/events', 'event' + str(count), putData)
    #     return render_template('index.html')
    # return render_template("home.html")
@app.route('/about')
def about():
    # colours = ['Red', 'Blue', 'Black', 'Orange']
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)
