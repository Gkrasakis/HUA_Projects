import os

from flask import Flask, redirect, url_for, request, render_template, flash, abort
from flask_bootstrap import Bootstrap5
import logging
from flask_wtf import CSRFProtect
from database import init_db, db_session

from models import Employee, LeaveRequest
from forms import EmployeeForm, LeaveRequestForm


#Configuring Logging to Record Debug Information to 'record.log' File
logging.basicConfig(filename="record.log", level=logging.DEBUG,datefmt= "%Y-%m-%d %H:%M:%S")

#Flask extensions BOOTSTRAP and CSRFProtect
app = Flask(__name__)
app.config.from_object('config')
# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)


#Intialization of the database within the context of a Flask application, ensuring proper configuration and access to application resources.
with app.app_context():
    init_db()


#Setting up a Random Secret Key for Flask Application Security (seasurf token)
#***************************************
import secrets

foo = secrets.token_urlsafe(16)
app.secret_key = foo
#***************************************

#Database Session Cleanup Function
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.close()
    
#Flask route decorator function
#Define routes and views


#(HOME PAGE)
#***************************************************************************************************************
@app.route('/')
def home():
    return render_template ('home.html')
#***************************************************************************************************************

#Employees
#***************************************************************************************************************
@app.route("/employees", methods=["GET"])
def show_employees():
    employees = Employee.query.all()
    return render_template("employees.html", employees=employees)


@app.route("/employee", methods=["GET", "POST"])
def show_employee_form():
    form = EmployeeForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        birth_year = form.birth_year.data
        email = form.email.data
        phone = form.phone.data
        job_position = form.job_position.data
        
        employee = Employee(
            name=name, 
            surname=surname, 
            birth_year=birth_year, 
            email=email, 
            phone=phone, 
            job_position=job_position
            )
        db_session.add(employee)
        db_session.commit()
        return redirect(url_for("show_employee_form"))
        #return redirect(url_for("show_users", users=users))
    return render_template("employee_form.html", form=form, message=message)
    
@app.route("/employee/<int:employee_id>", methods=["GET", "POST"])
def show_employee_form_update(employee_id):
    message = ""
    employee = Employee.query.filter(Employee.id == employee_id).first()
    if not employee:
        return render_template("404.html", title="404"), 404
    form = EmployeeForm(obj=employee)
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        birth_year = form.birth_year.data
        email = form.email.data
        phone = form.phone.data
        job_position = form.job_position.data
        employee.name = name
        employee.surname = surname
        employee.birth_year = birth_year
        employee.email = email
        employee.phone = phone
        employee.job_position = job_position
        db_session.commit()
        return redirect(url_for("show_employees"))
    return render_template("employee_form.html", form=form, message=message, employee=employee)

#***************************************************************************************************************

#Employees_Requests
#***************************************************************************************************************
@app.route("/requests", methods=["GET"])
def show_requests():
    leave_requests = LeaveRequest.query.all()
    return render_template("requests.html", leave_requests=leave_requests)

@app.route('/request/<uid>', methods=['GET','POST'])
def show_request_form(uid):
    message = ""
    employee = Employee.query.filter(Employee.id == uid).first()
    form = LeaveRequestForm(employee=employee)
    
    if form.validate_on_submit():
        start_date = form.start_date.data
        end_date = form.end_date.data
        reason = form.reason.data
        
        request = LeaveRequest(
            start_date=start_date, 
            end_date=end_date, 
            reason=reason, 
            employee=employee
        )
        db_session.add(request)
        db_session.commit()
        
        leave_requests = employee.leave_requests
        
        flash('Record was successfully added')
        
        return render_template("employee_requests.html", employee=employee, leave_requests=leave_requests)
    return render_template("employee_form.html", form=form, message=message, employee=employee)


@app.route("/request/<uid>/<jid>/delete", methods = ["GET"])
def delete_request(uid, jid):
    employee = Employee.query.filter(Employee.id == uid).first()
    leaveRequest = LeaveRequest.query.filter(LeaveRequest.id == jid).first()
    db_session.delete(leaveRequest)
    employee.leave_requests.remove(leaveRequest)
    db_session.commit()
    leave_requests = employee.leave_requests
    return render_template("employee_requests.html", employee=employee, leave_requests=leave_requests)

@app.route("/requests/<employee_id>", methods=["GET"])
def show_employee_requests(employee_id):
    employee = Employee.query.filter(Employee.id == employee_id).first()
    requests = employee.leave_requests
    return render_template("employee_requests.html", employee=employee, requests=requests)

@app.route("/request/<jid>", methods=["DELETE"])
def delete_request_by_id(jid):
    request = LeaveRequestForm.query.filter(LeaveRequestForm.id == jid).first()
    employee = LeaveRequestForm.employee

    print(request)
    db_session.delete(request)
    db_session.commit()
    requests = employee.requests
    return render_template("employee_requests.html", employee=employee, requests=requests)
#***************************************************************************************************************


#Error handlers
#******************************************************************************************************
@app.errorhandler(404)
def not_found_error():
    return render_template('404.html'), 404

@app.errorhandler(Exception)
def internal_error():
    return render_template('404.html'), 500
##***************************************************************************