from flask import render_template, redirect,url_for,abort
# from flask_login import login_required, current_user
from . import main
# from .forms import BlogForm, CommentForm, SubscriberForm
# from ..models import Blog, Comment, User, Subscriber
# from ..email import mail_message
# from .. import db
# import markdown2

@main.route('/')
def index():
    '''
    function that returns the index page
    '''
    record = 'health records'
    return render_template('index.html', record = record)
