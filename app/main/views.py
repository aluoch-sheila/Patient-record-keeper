from flask import render_template, redirect,url_for,abort
from flask_login import login_required, current_user
from . import main
from ..models import User,Patient,Record
# from ..email import mail_message
from .. import db
from .. import auth
from . forms import LoginForm,PatientForm,RecordForm
# import markdown2

@main.route('/',methods = ['GET','POST'])
@login_required
def index():
    '''
    function that returns the index page
    '''
    patients = Patient.query.all()
    return render_template('index.html', patients = patients)


@main.route('/user/<uname>')
@login_required

def profile(uname):
    user = User.query.filter_by(username = uname).first()
    # abort(404)

    # post = Blog.query.filter_by(user_id = current_user.id).all()
    # print(post)


    title = uname

    return render_template('profile.html', user = user)

@main.route('/new_patient', methods = ['GET','POST'])
@login_required
def new_patient():
   form  =PatientForm()

   if form.validate_on_submit():
       patient = form.patient.data

       new_patient = Patient(patient = patient, user_id = current_user.id)

       new_patient.save_patient()

       return redirect(url_for('main.index'))

   title = 'New Patient'
   return render_template('new_patient.html',title = title, patient_form = form)


@main.route('/record/<id>')
def record(id):
    '''
    function to return the records
    '''
    record = Record.get_record(id)
    print(record)
    title = 'patient records'
    return render_template('record.html',title = title, record = record)



@main.route('/new_record/<int:id>', methods = ['GET', 'POST'])
def new_record(id):
    form = RecordForm()

    if form.validate_on_submit():
        writer = form.docter.data
        record = form.record.data

        new_record = Record(record = record, patient_id = id, docter= writer)
        new_record.save_record()

        return redirect(url_for('main.index'))

    title = 'New Record'
    return render_template('new_record.html', title = title, record_form = form)
