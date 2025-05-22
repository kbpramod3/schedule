from datetime import datetime, timedelta

def time_diff(start, end):
    fmt = "%H:%M"
    start_dt = datetime.strptime(start, fmt)
    end_dt = datetime.strptime(end, fmt)
    return int((end_dt - start_dt).total_seconds() / 60)

schedule = {
    "Workout (A10)": {"start": "07:00", "end": "08:00", "category": "Personal"},
    "Breakfast": {"start": "08:00", "end": "08:30", "category": "Meal"},
    "Kids Carpool (A8)": {"start": "08:30", "end": "09:30", "category": "Personal"},
    "Email Time (A3)": {"start": "09:30", "end": "10:00", "category": "Work"},
    "Commute to Office": {"start": "10:00", "end": "10:30", "category": "Commute"},
    "Team Standup (A7)": {"start": "10:30", "end": "11:00", "category": "Work"},
    "Meet James (A6)": {"start": "11:00", "end": "11:30", "category": "Work"},
    "Customer Meetings (A2)": {"start": "11:30", "end": "12:30", "category": "Work"},
    "Lunch": {"start": "12:30", "end": "13:30", "category": "Meal"},
    "Email Time (A3)": {"start": "13:30", "end": "14:00", "category": "Work"},
    "Conference Call (A1)": {"start": "14:00", "end": "15:00", "category": "Work"},
    "Customer Meetings (A2)": {"start": "15:00", "end": "16:00", "category": "Work"},
    "Prepare Pitch (A5)": {"start": "16:00", "end": "16:30", "category": "Work"},
    "Independent Work (A4)": {"start": "16:30", "end": "17:30", "category": "Work"},
    "Commute to Home": {"start": "17:30", "end": "18:00", "category": "Commute"},
    "Dentist Appointment (A9)": {"start": "18:00", "end": "19:00", "category": "Personal"},
    "Dinner": {"start": "19:30", "end": "20:30", "category": "Meal"},
    "Research Holiday (A11)": {"start": "20:30", "end": "21:30", "category": "Personal"},
    "Family Time (A12)": {"start": "21:30", "end": "22:00", "category": "Personal"},
    "General Admin (A13)": {"start": "22:00", "end": "22:30", "category": "Personal"},
    "General Admin (A13)": {"start": "22:30", "end": "23:00", "category": "Personal"}
}


total_activity_minutes = 0
personal_minutes = 0

for activity, details in schedule.items():
    duration = time_diff(details["start"], details["end"])
    if details["category"] in ["Work", "Personal"]:
        total_activity_minutes += duration
        if details["category"] == "Personal":
            personal_minutes += duration

personal_allocation_percentage = round((personal_minutes / total_activity_minutes) * 100)

assignments = {
    activity: {"start": details["start"], "end": details["end"]}
    for activity, details in sorted(schedule.items(), key=lambda x: x[1]["start"])
}

print(assignments, personal_allocation_percentage)
