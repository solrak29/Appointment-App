from model import Provider, Users, connect_to_db,db, Client, Appointment, AppointmentType
from datetime import datetime, timedelta
from sqlalchemy import select
from data import NewEntry
from excpetions import NonProviderException

def verify_user(user_name):
    user_data = []
    rows = db.session.query(Users.user_id).filter_by(user_name = user_name).all()
    if len(rows) > 1:
         return False
    return True

def verify_user_pass(user_name, password):
    stmt = select(Users).where(Users.user_name == user_name, Users.password == password)
    rows = db.session.execute(stmt)
    print(rows)
    return True if rows else False


def create_new_entry( entry: NewEntry):
    """
	Utility function that will create a new client for a provider.
    Steps:
    1.  Verifty provider is listed in the DB.
    2.  Create User as potential client and link to provider through Client table.
    3.  Mark as inactive (inactive users can do anything) note: config can set this as default
    """

    provider = Provider.query.filter_by(provider_name=entry.provider)

    if not (provider):  raise NonProviderException(entry.provider)

    """This function is to create a new Client"""
    new_entry = Client(first_name=first_name, 
					   last_name=last_name, 
					   email=email, 
					   cell_phone_number=cell_phone_number, 
					   user_name=user_name,
					   password=password,
					   is_admin=1 if is_admin == "on" else 0)
	#  The idea here is that we can several business owners using this tool
    #  So we have this boject to where they can see other options and manage some busines owner options.
    #  One other user will be the super user which will be the person managins all business
    

    db.session.add(new_entry)
    db.session.commit()
    return new_entry 

def create_new_appt(user_id,appt_type_id,appt_time,provider_id,appt_date):
	"""This function is to create a new appointment"""
	new_appt = Appointment(user_id=user_id, appt_type_id=appt_type_id,appt_time=appt_time, provider_id= provider_id, appt_date=appt_date)
	db.session.add(new_appt)
	db.session.commit()
	return new_appt

def create_appt_type(appt_type,cost):
	"""two types of appointments"""
	appt_type = AppointmentType(appt_type= appt_type, cost= cost)
	db.session.add(appt_type)
	db.session.commit()
	return appt_type


def create_new_user(first_name, last_name, address, phone_number, user_name, password):
    user_id = verify_user(user_name)
    if user_id:
        return user_id
    else:
        new_user = Users(first_name=first_name,
				         last_name=last_name,
					     address=address,
					     phone=phone_number,
					     user_name=user_name,
					     password=password)
        db.session.add(new_owner)
        db.session.commit()
        return(verify_user(user_name))

def create_new_owner(first_name,last_name,address,phone_number, user_name, password):
	"""This is to create a new owner"""
	new_owner = Provider(first_name=first_name,
				  last_name=last_name,
			          address=address,
				  phone=phone_number,
                                  user_name=user_name,
                                  password=password)
	db.session.add(new_owner)
	db.session.commit()
	return new_owner