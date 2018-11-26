from flask import render_template, redirect,url_for,abort
from flask_login import login_required, current_user
from . import main
from ..models import User
# from ..email import mail_message
from .. import db
# import markdown2

@main.route('/')
@login_required
def index():
    '''
    function that returns the index page
    '''
    record = 'health records'
    return render_template('index.html', record = record)
