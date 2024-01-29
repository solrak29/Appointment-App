""" Appointment Scheduling and Confirmation""" 

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, session, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from helper.calander_helper import generate_calander
from model import connect_to_db, db, Client,Appointment, AppointmentType, BusinessOwner
from database_functions import create_new_entry, create_new_appt, create_appt_type, create_new_owner, verify_user
from datetime import datetime,timedelta
import json
from twilio.rest import TwilioRestClient
from datetime import date

app = Flask(__name__)

app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """ This is the homepage"""
    return render_template("homepage.html")

@app.route('/registration', methods=['GET'])
def registration():
    return render_template('registration.html')

@app.route('/login', methods=['GET'])
def login():
    """This will allow the business owner and Client to log in. Show the forms"""
    return render_template("login.html")

@app.route('/register', methods=['POST'])
def login_process():
    """
    Creates a new user:
    The user can be an admin (the business owner) or a client ofthe business.
    TODO:  Have a verification check for when is_admin is set and the account has to be verfied first.
    TODO:  Email verification where the client can authenticate themselves.
    TODO:  2-factor authentication will be needed.
    """
    #Getting the variables
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email= request.form.get("email")
    cell_phone_number = request.form.get("cell_phone_number")
    user_name = request.form.get("user_name")
    password = request.form.get("password")
    is_admin = request.form.get("is_admin")

    _ = create_new_entry(first_name=first_name, 
                         last_name=last_name, 
                         email=email, 
                         cell_phone_number=cell_phone_number, 
                         user_name=user_name,
                         password=password,
                         is_admin=is_admin)
    # The idea here is that create_new_entry will not be 100% complete if admin is selected.
    # TODO: When admin is selected we should have the account verified.  If the account is not verified
    #       Then we should provide the appropiate message.
    #       Once verifed we provide the admin page that will show the schedule for the business.

    if is_admin:
        today = date.today()
        #taken_appts=Appointment.query.filter_by(appt_date=today).join(Client,Appointment.user_id==Client.user_id).add_columns(Appointment.appt_id, Appointment.provider_id, Appointment.user_id, Appointment.appt_time, Appointment.appt_type_id, Appointment.appt_date, Client.first_name, Client.last_name).all()    
        cal_data = generate_calander(today.year, today.month, None)
        return render_template ("appt_book.html", cal_data=cal_data, taken_appts=None, day=today.day, year=today.year, month=today.month, isDoctor=is_admin)
    else:
        return render_template("existing_user_page.html", first_name=first_name)

@app.route('/existing_user_login', methods=['GET'])
def show_options_for_user():
    """ show existing user a page to choose from two options"""
    
    user_name=request.args.get('user_name')
    password= request.args.get('password')
    Client= Client.query.filter_by(user_name=user_name).first

    return redirect('existing_user_page.html')

#@app.route('/owner_login', methods=['POST'])
#def show_appt_book_to_owner():
#    """Display the appointments scheduled for the owner to see"""
#    time_now= datetime.now()
#    day= time_now.day
#    month= time_now.month
#    year= time_now.year
#
#    session['isDoctor'] = True
#
#    return redirect("/appt_book?appt_day=%s&appt_month=%s&appt_year=%s"%(day,month,year))

@app.route('/login', methods=['POST'])
def show_appts_scheduled_for_this_pt():
    """ show the user all the appointments that he/she has scheduled"""
    
    user_name= request.form.get('user_name')
    password=request.form.get('password')
    client = Client.query.filter_by(user_name=user_name).first()
    if not client:
        flash("Please enter the correct password!")
        return redirect ('plogin')

    first_name = client.first_name

    if client.password == password:
        user_id= client.user_id
        session['user_id']= user_id
        session['isDoctor'] = False

        return render_template("existing_user_page.html", first_name=first_name)
    else:
        flash("Please enter the correct password!")
        return redirect ('plogin')


@app.route('/reviews/', methods=['GET'])
def show_review_page():
    """Display reviews page"""

    return render_template("reviews.html")

@app.route('/owner_login', methods=['GET'])
def owner_page():
    """Display form for owner
    This will display the page to allow the owner of the appointment setup
    to login or provide a new owner to create their profile and generate their
    own system.
    """
    return render_template("owner_login.html", status='ok')


@app.route('/owner_login', methods=['POST'])
def owner_login():
    """Login for Admin role
    This allows an owner to login and see thier appiontments.
    """
    user_name=request.form["user_name"]
    password=request.form["password"]
    if verify_user(user_name, password):
        return render_template("owner_login.html", status='Verified')
    else:
        return render_template("owner_login.html", status='Not Verified')


@app.route('/new_owner_login', methods=['POST'])
def new_owner_login():
    """Process owner login
    This page will allow someone to sign up for the produce.  Upon
    any entry for someone to create the produce, the idea here is walk
    through "wizards" or automate copying template files to generate
    the web site the user will need to handle appointments.
    """
    print(request.form)
    first_name=request.form["first_name"]
    last_name=request.form["last_name"]
    address=request.form["address"]
    phone_number=request.form["phone_number"]
    user_name=request.form["user_name"]
    password=request.form["password"]
    new_owner= create_new_owner(first_name=first_name,
                                last_name=last_name,
                                address=address,
                                phone_number=phone_number,
                                user_name=user_name,
                                password=password)
    db.session.add(new_owner)
    db.session.commit()
    return render_template("owner_login.html", status="New User")


@app.route ('/appt_book', methods=['GET'])
def show_appt_book():
    """This will take the pts name and show the appt book"""

    appt_day = int(request.args.get('appt_day'))
    appt_month = int(request.args.get('appt_month'))
    appt_year = int(request.args.get('appt_year'))
    
    isDoctor = False
    if 'isDoctor' in session:
        isDoctor = session['isDoctor']

    search_date = "%s/%s/%s"%(appt_month,appt_day,appt_year)

    taken_appts=Appointment.query.filter_by(appt_date=search_date).join(Client,Appointment.user_id==Client.user_id).add_columns(Appointment.appt_id, Appointment.provider_id, Appointment.user_id, Appointment.appt_time, Appointment.appt_type_id, Appointment.appt_date, Client.first_name, Client.last_name).all()    
    cal_data = generate_calander(appt_year, appt_month, taken_appts)
    return render_template ("appt_book.html", cal_data=cal_data, taken_appts=taken_appts, day=appt_day, year=appt_year, month=appt_month, isDoctor=isDoctor)

@app.route ('/appt_book/<year>/<month>/<day>/<provider_id>/<timeslot>', methods=['POST'])
def appt_book_view(year,month,day,provider_id,timeslot):
    """Appointment book view"""

    fullDate = str(month)+'/'+str(day)+'/'+str(year)

    isDoctor = False
    if 'isDoctor' in session:
        isDoctor = session['isDoctor']

    created_appt= create_new_appt(session['user_id'],1,str(timeslot),provider_id,str(fullDate))
    db.session.add(created_appt)
    db.session.commit()
    print("Appointment saved")
    return redirect('/confirm_appt')


@app.route ('/confirm_appt', methods=['GET'])
def show_scheduled_appts():
    """ Display page to show what is scheduled for this user"""
    user_id= session['user_id']
    Client = Client.query.filter_by(user_id=user_id).first()
    first_name = Client.first_name

    appointments= Appointment.query.filter_by(user_id=user_id).all()
    twilio(user_id)

    return render_template("/confirmed.html",first_name=first_name,appointments=appointments)

@app.route ('/confirm_appt', methods=['POST'])
def conf_appt():
    """ Need to send user to another page after appt has been confirmed"""
    provider_id=request.form.get('provider_id')
    appt_time=request.form.get('appt_time')
    day= request.form.get('day')
    month= request.form.get('month')
    year= request.form.get('year')
    appt_date="%s/%s/%s"%(month,day,year)
    user=session['user_id']

    Client = Client.query.filter_by(user_id=user).first()
    user_id =Client.user_id 
    first_name=Client.first_name
    created_appt= create_new_appt(user_id=user_id,
                            appt_type_id=1,
                            appt_time=appt_time,
                            provider_id=provider_id,
                            appt_date=appt_date)
    

    appointments= Appointment.query.filter_by(user_id=user_id).all()
    return "Your appointment has been saved!"

# @app.route('/twilio/<int:user_id>', methods=['POST'])
def twilio(user_id):


    appointment= Appointment.query.get(user_id)
    Client= Client.query.get(user_id)
    cell_phone_number= Client.cell_phone_number
    print(cell_phone_number)
    body = "Hello "+(Client.first_name)+" We look forward to seeing you on "+(appointment.appt_date)+"at "+(appointment.appt_time)


    account_sid = "AC38e1b6d5cc02a5b6eb36e4c446693f57"
    auth_token = "1d21cdeed73e33a78fe10a8103024972 "
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to=cell_phone_number, from_="+16506845238",
                                    body=body)
    flash("Your message was sent successfully.")
    return redirect("/confirmed.html") 



if __name__ == "__main__":
    
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host='0.0.0.0')





