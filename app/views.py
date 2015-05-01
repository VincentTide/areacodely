from app import app
from flask import request, session, render_template, redirect, url_for, flash, abort
from forms import *
from models import *
from datetime import datetime
from sqlalchemy import desc, asc


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/', methods=['GET'])
def index():
    form = TelephoneForm()
    return render_template('index.html', form=form)

@app.route('/contact-us', methods=['GET'])
def contact():
    return render_template('contact.html')







