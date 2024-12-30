from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, IntegerField, EmailField, DateField
from wtforms.validators import DataRequired, Length, Email

class EmployeeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(3, 15)])
    surname = StringField('Surname', validators=[DataRequired(), Length(3, 20)])
    birth_year = IntegerField('Birth Year', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    job_position = StringField('Job Position', validators=[DataRequired()])
    submit = SubmitField('Submit')

    
class LeaveRequestForm(FlaskForm):
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    reason = StringField('Reason', validators=[DataRequired(), Length(50, 180)])
    submit = SubmitField('Submit')   
    
