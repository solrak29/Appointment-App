import pytest
from datetime import datetime
from model import Users, connect_to_db, db, Provider, UserType, load_user_types
from server import app

"""
Test configuartions for pytest to setup the test db (i.e. sqllite)
"""

@pytest.fixture
def connect_to_test_db():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_booking_system.db'
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()
        load_user_types()
        yield db

def create_user_types(db) -> UserType:
    user_type = UserType(
        type_desc = "test user type",
        create_date = datetime.now(),
        update_date = datetime.now()
    )
    db.session.add(user_type)
    db.session.commit()
    new_user_type = UserType.query.filter_by(type_desc="test user type").first()
    return new_user_type


def create_random_user(db) -> Users:
    user_type = create_user_types(db)
    new_user = Users(first_name="Davis",
				     last_name="Joens",
                     user_type_id = user_type.type_id,
					 street_address="101 Elm Street",
                     city = "somecity",
                     state = "some state",
					 cell_phone_number="222-222-2222",
                     email="some email",
					 user_name="davis",
					 password="davis",
                     create_date=datetime.now(),
                     update_date=datetime.now())
    db.session.add(new_user)
    db.session.commit()
    new_user = Users.query.filter_by(user_name="davis").first()
    return new_user


@pytest.fixture
def seed_provider_data():
    # create provider for testing
    user = create_random_user()
    new_provider = Provider(
         user_id = user.user_id,
         provider_name = "ToonPet",
         create_date = datetime.now(),
         update_date = datetime.now(),
    )
    db.session.add(new_provider)
    db.session.commit()


@pytest.fixture
def seed_user_data(connect_to_test_db):
    # create single user fo rthe table Users
    create_random_user(connect_to_test_db)