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
    form = TelephoneForm()
    return render_template('search.html', form=form)

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
        # Tell user we didnt find any results
        entry = {}
        if location is None:
            entry = {
                "area_code": area_code,
                "central_office_code": central_office_code
            }
            return render_template('search.html',
                                   form=form,
                                   entry=entry)

        # A successful result is found
        else:
            # Format dates for human readers
            if location.date_assigned is not None:
                location.date_assigned = location.date_assigned.strftime('%m/%d/%Y')
            else:
                location.date_assigned = ""
            if location.date_effective is not None:
                location.date_effective = location.date_effective.strftime('%m/%d/%Y')
            else:
                location.date_effective = ""

            # If we have no data, show as blank
            if location.full_name is None:
                location.full_name = ""
            if location.metro is None:
                location.metro = ""

            # Google maps search query
            query = "%s %s" % (location.full_name, location.state)
            query = query.split()
            query = "+".join(query)
            google_maps = "http://maps.google.com/?q=%s" % query

            return render_template('search.html',
                                   location=location,
                                   form=form,
                                   google_maps=google_maps,
                                   entry=entry)
    return render_template('search.html',
                           form=form)




