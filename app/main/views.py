from flask import render_template, request, redirect, url_for, abort
from . import main

from .. import db


@main.route('/')
def index():
 title = 'Home - Welcome to Tabibu'

 return render_template('index.html', title=title)


@main.route('/about')
def about():
 title = 'Home - Welcome to Tabibu'

 return render_template('about.html', title=title)


@main.route('/team')
def team():
 title = 'Home - Welcome to Tabibu'

 return render_template('team.html', title=title)


@main.route('/contact')
def contact():
 title = 'Home - Welcome to Tabibu'

 return render_template('contact.html', title=title)

