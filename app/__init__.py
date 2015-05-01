from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.moment import Moment

app = Flask(__name__)
app.config.from_object('config')

# Make sure we declare db first before importing views or models
db = SQLAlchemy(app)

# Extensions initialization
moment = Moment(app)

# Import views at the end
from app import views
