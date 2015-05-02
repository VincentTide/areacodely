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

@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search_post():
    form = TelephoneForm()
    if form.validate_on_submit():
        number = form.number.data.strip()
        # Check that number is exactly 6 digits
        area_code = int(number[0:3])
        central_office_code = int(number[3:6])
        location = Telephone.query.filter_by(area_code=area_code,
                                             central_office_code=central_office_code).first()
        # If we don't find it
        if location is None:
            # tell user we didnt find it
            flash("No data found for (NPA) NXX")
            return redirect(url_for('index'))
        else:
            # give user the data
            return render_template('search.html',
                                   location=location,
                                   form=form)
    return render_template('search.html', location=None, form=form)




