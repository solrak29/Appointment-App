import calendar

def generate_calander(year, month, appts):
    cal = calendar.monthcalendar(year, month)
    calendar_data = []

    for week in cal:
        week_data = []
        for day in week:
            day_data = {"day": day, "appt": []}
            if appts:
                for appt in appts:
                    appt_date = appt["date"]
                    if appt_date.year == year and appt_date.month == month:
                        day_data["appt"].append(appt)
            week_data.append(day_data) 
        calendar_data.append(week_data)

    return calendar_data