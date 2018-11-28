from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import db, login_manager
from datetime import datetime


class User(UserMixin,db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    patient = db.relationship('Patient', backref = 'username', lazy = 'dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f' {self.username}'


class Patient(db.Model):

    __tablename__ = 'patients'

    id = db.Column(db.Integer,primary_key = True)
    patient = db.Column(db.Integer)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    def save_patient(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_patient(cls, user_id):
        patient = Patient.query.filter_by(id=user_id).all()
        return patient



class Record(db.Model):

    __tablename__ = 'records'

    id = db.Column(db.Integer, primary_key=True)
    record = db.Column(db.String)
    docter = db.Column(db.String(255))
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"))

    def save_record(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_record(cls, id):
        record = Record.query.filter_by(patient_id=id).all()
        return record

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
