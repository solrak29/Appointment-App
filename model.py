"""Models and database functions for my app"""

import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()


class UserType(db.Model):
    __tablename__ = 'user_type'
    type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type_desc = db.Column(db.String(100), nullable=False)
    create_date = db.Column(db.Date(), nullable=False)
    update_date = db.Column(db.Date(), nullable=False)

def load_user_types():
    user_types = UserType( type_desc="Toon Pet Client",
                          create_date= datetime.datetime.now(),
                          update_date = datetime.datetime.now())
    db.session.add(user_types)
    user_types = UserType( type_desc="Toon Pet Owner",
                          create_date= datetime.datetime.now(),
                          update_date = datetime.datetime.now())
    db.session.add(user_types)
    db.session.commit()

class Users(db.Model):
    """All users of the system"""
    __tablename__ = "users"
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String(64), nullable=False)
    user_type_id = db.Column(ForeignKey(UserType.type_id))
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String, nullable=False) 
    cell_phone_number = db.Column(db.String(64), nullable=False)
    user_name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    street_address = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    state = db.Column(db.String(64), nullable=False)
    create_date = db.Column(db.Date(), nullable=False)
    update_date = db.Column(db.Date(), nullable=False)

class Provider(db.Model):
    """ Provider Details"""
    __tablename__ = "provider"

    provider_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(ForeignKey(Users.user_id))
    provider_name = db.Column(db.String(64), nullable=False)
    create_date = db.Column(db.Date(), nullable=False)
    update_date = db.Column(db.Date(), nullable=False)


class Client(db.Model):
    """Client registration info"""

    __tablename__ = "client"

    client_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(ForeignKey(Users.user_id))
    provider_id = db.Column(ForeignKey(Provider.provider_id))
    is_provider = db.Column(db.Integer, nullable=False)
    appointments = db.relationship("Appointment")


class Appointment(db.Model):
    """All Appointment info for my table"""

    __tablename__ = "appointment"

    appt_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('client.user_id'), nullable=False)
    appt_time = db.Column(db.String, nullable=False)
    appt_date = db.Column(db.String, nullable=False)
    appt_type_id = db.Column(db.Integer, db.ForeignKey('appointment_type.appt_type_id'), nullable=False)
    provider_id = db.Column(db.Integer,db.ForeignKey('provider.provider_id'),nullable=False )

    def as_dict(self):
    	return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class AppointmentType(db.Model):
    """Two different appointment types"""

    __tablename__ = "appointment_type"
    appt_type_id = db.Column(db.Integer, primary_key=True)
    appt_type = db.Column(db.String, nullable=False)
    cost = db.Column(db.Integer, nullable=False)


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # we can choose a database later but for now let's use sqllite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booking_system.db'
    
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()
        load_user_types()
    

if __name__ == "__main__":
    
    from server import app
    connect_to_db(app)
    print("Connected to DB.")
