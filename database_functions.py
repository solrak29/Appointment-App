from model import connect_to_db,db, Client, BusinessOwner, Appointment, AppointmentType
from datetime import datetime, timedelta
from sqlalchemy import select

def verify_user(user_name, password):
    stmt = select(BusinessOwner).where(BusinessOwner.user_name == user_name)
    rows = db.session.execute(stmt)
    print(rows)
    if rows:
        return True
    else:
        False

def create_new_entry(first_name,
				     last_name,
				     email,
				     cell_phone_number,
				     user_name,
				     password,
				     is_admin):


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


def create_new_owner(first_name,last_name,address,phone_number, user_name, password):
	"""This is to create a new owner"""
	new_owner = BusinessOwner(first_name=first_name,
				  last_name=last_name,
			          address=address,
				  phone=phone_number,
                                  user_name=user_name,
                                  password=password)
	db.session.add(new_owner)
	db.session.commit()
	return new_owner