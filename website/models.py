from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    screens = db.relationship('Screen')

class Screen(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    driver = db.Column(db.String(150), unique=True)
    co_driver = db.Column(db.String(150))
    service_IN = db.Column(db.String(150))
    service_OUT = db.Column(db.String(150))
    service_time = db.Column(db.Float)
    margin_time = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))