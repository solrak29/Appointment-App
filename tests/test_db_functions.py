
from model import Provider
from database_functions import verify_user

def test_new_entry(seed_provider_data):
    p = Provider.query.filter_by("ToonPet")
    print(p)

def test_verify_user(connect_to_test_db, seed_user_data):
    assert verify_user("davis") == True