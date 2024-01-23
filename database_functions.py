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

def create_new_pt(first_name,
				  last_name,
				  date_of_birth,
				  cell_phone_number,
				  user_name,
				  password):


	"""This function is to create a new Client"""
	the_client = Client(first_name=first_name, 
					last_name=last_name, 
					date_of_birth=date_of_birth, 
					cell_phone_number=cell_phone_number, 
					user_name=user_name,
					password=password)
	db.session.add(the_client)
	db.session.commit()

	return the_client

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

def next_aval_date():
	"""returns the first available date for user

		>>> type(next_aval_date())
		<type 'tuple'>

	"""
	time_now= datetime.now()
	td= timedelta(1)

	first_available_day = time_now + td 
	weekdays= ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
	for day in weekdays:
		if day in weekdays:
			first_available_day= time_now +td
		else: 
			first_available_day= time_now +timedelta(3)
	return (first_available_day.day, first_available_day.month, first_available_day.year)






