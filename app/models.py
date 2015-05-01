from app import app, db
from datetime import datetime


class Telephone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.Text)
    state = db.Column(db.Text)
    area_code = db.Column(db.Integer)
    central_office_code = db.Column(db.Integer)
    rate_center = db.Column(db.Text)
    full_name = db.Column(db.Text)
    metro = db.Column(db.Text)
    assigned_to = db.Column(db.Text)
    date_assigned = db.Column(db.DateTime)
    date_effective = db.Column(db.DateTime)






