'''
Author: Ms Rya
Version: 3.10
'''
import sqlite3

class Courier:
    def __init__(self, courier_id, reference_number, sender_name, send_date, courier_type, contact_info, tracking_number, delivery_status):
        self.courier_id = courier_id
        self.reference_number = reference_number
        self.sender_name = sender_name
        self.send_date = send_date
        self.courier_type = courier_type
        self.contact_info = contact_info
        self.tracking_number = tracking_number
        self.delivery_status = delivery_status

    def display(self):
        return (f"Courier ID: {self.courier_id}\t"
                f"Reference Number: {self.reference_number}\t"
                f"Sender Name: {self.sender_name}\t"
                f"Send Date: {self.send_date}\t"
                f"Courier Type: {self.courier_type}\t"
                f"Contact Info: {self.contact_info}\t"
                f"Tracking Number: {self.tracking_number}\t"
                f"Delivery Status: {self.delivery_status}\n")


class Visitor:
    def __init__(self, name, contact_number, visitor_pass, government_id, purpose_of_visit, person_meeting, department):
        self.name = name
        self.contact_number = contact_number
        self.visitor_pass = visitor_pass
        self.government_id = government_id
        self.purpose_of_visit = purpose_of_visit
        self.person_meeting = person_meeting
        self.department = department

    def visitor_display(self):
        return (f"Name: {self.name}\n"
                f"Contact Number: {self.contact_number}\n"
                f"Visitor Pass: {self.visitor_pass}\n"
                f"Government ID: {self.government_id}\n"
                f"Purpose of Visit: {self.purpose_of_visit}\n"
                f"Meeting: {self.person_meeting}\n"
                f"Department: {self.department}\n")


class InterviewCall:
    def __init__(self, candidate_name, role_applied_for, interview_date_time, interviewers_name, interviewers_department):
        self.candidate_name = candidate_name
        self.role_applied_for = role_applied_for
        self.interview_date_time = interview_date_time
        self.interviewers_name = interviewers_name
        self.interviewers_department = interviewers_department

    def call_display(self):
        return (f"Candidate Name: {self.candidate_name}\n"
                f"Role Applied For: {self.role_applied_for}\n"
                f"Interview Date and Time: {self.interview_date_time}\n"
                f"Interviewer’s Name: {self.interviewers_name}\n"
                f"Interviewer’s Department: {self.interviewers_department}\n")




conn = sqlite3.connect('ICR_SQL1.db')
sth = conn.cursor()


sth.execute('''
Create table if not exists
Courier(
    courier_id TEXT PRIMARY KEY ,
    reference_number TEXT,
    sender_name TEXT,
    send_date TEXT,
    courier_type TEXT,
    contact_info TEXT,
    tracking_number TEXT,
    delivery_status TEXT
)

       ''')

# Creating Visitor objects
sth.execute('''
create table if not exists
Visitor(
    name TEXT,
    contact_number TEXT,
    visitor_pass TEXT,
    government_id TEXT,
    purpose_of_visit TEXT,
    person_meeting TEXT,
    department TEXT
)
''')


# Creating InterviewCall objects
sth.execute('''
create table if not exists
InterviewCall(
    candidate_name TEXT,
    role_applied_for TEXT,
    interview_date_time TEXT,
    interviewers_name TEXT,
    interviewers_department TEXT
    )
''')

print('Tables have been created!!')


courier1 = Courier(
    courier_id='C001',
    reference_number='R12345',
    sender_name='Arun',
    send_date='14th March',
    courier_type='Email',
    contact_info='arun@example.com',
    tracking_number='T123456789',
    delivery_status='Delivered'
)

courier2 = Courier(
    courier_id='C002',
    reference_number='R67890',
    sender_name='Matt',
    send_date='3rd May',
    courier_type='Courier',
    contact_info='matt@example.com',
    tracking_number='T987654321',
    delivery_status='In Transit'
)

sth.execute('''
insert into Courier(courier_id,reference_number,sender_name,send_date,courier_type,contact_info,tracking_number,delivery_status)
values(?,?,?,?,?,?,?,?)
''', (courier1.courier_id,
      courier1.reference_number,
      courier1.sender_name,
      courier1.send_date,
      courier1.courier_type,
      courier1.contact_info,
      courier1.tracking_number,
      courier1.delivery_status))

sth.execute('''
insert into Courier(courier_id,reference_number,sender_name,send_date,courier_type,contact_info,tracking_number,delivery_status)
values(?,?,?,?,?,?,?,?)
''', (courier2.courier_id,
      courier2.reference_number,
      courier1.sender_name,
      courier2.send_date,
      courier2.courier_type,
      courier2.contact_info,
      courier2.tracking_number,
      courier2.delivery_status))

print("Courier 1:")
print(courier1.display())

print("\nCourier 2:")
print(courier2.display())

visitor1 = Visitor(
    name='Alice',
    contact_number='123-456-7890',
    visitor_pass='V001',
    government_id='ID123456789',
    purpose_of_visit='Business Meeting',
    person_meeting='Bob',
    department='Sales'
)

visitor2 = Visitor(
    name='John',
    contact_number='987-654-3210',
    visitor_pass='V002',
    government_id='ID987654321',
    purpose_of_visit='Client Meeting',
    person_meeting='Sarah',
    department='Marketing'
)

sth.execute('''
insert into Visitor(name,contact_number,visitor_pass,government_id,purpose_of_visit,person_meeting,department)
values(?,?,?,?,?,?,?)
''', (visitor1.name,
      visitor1.contact_number,
      visitor1.visitor_pass,
      visitor1.government_id,
      visitor1.purpose_of_visit,
      visitor1.person_meeting,
      visitor1.department))
sth.execute('''
insert into Visitor(name,contact_number,visitor_pass,government_id,purpose_of_visit,person_meeting,department)
values(?,?,?,?,?,?,?)
''', (visitor2.name,
      visitor2.contact_number,
      visitor2.visitor_pass,
      visitor2.government_id,
      visitor2.purpose_of_visit,
      visitor2.person_meeting,
      visitor2.department))
print("\nVisitor 1:")
print(visitor1.visitor_display())

print("\nVisitor 2:")
print(visitor2.visitor_display())


interview1 = InterviewCall(
    candidate_name="Alice Smith",
    role_applied_for="Software Developer",
    interview_date_time="2024-08-15 14:00",
    interviewers_name="Bob Johnson",
    interviewers_department="Engineering"
)

interview2 = InterviewCall(
    candidate_name="Jake Lee",
    role_applied_for="Product Manager",
    interview_date_time="2024-08-20 10:00",
    interviewers_name="Emma Davis",
    interviewers_department="Marketing"
)

sth.execute('''
insert into InterviewCall(candidate_name,role_applied_for,interview_date_time,interviewers_name,interviewers_department)
values(?,?,?,?,?)
''', (interview1.candidate_name,
      interview1.role_applied_for,
      interview1.interview_date_time,
      interview1.interviewers_name,
      interview1.interviewers_department))
sth.execute('''
insert into InterviewCall(candidate_name,role_applied_for,interview_date_time,interviewers_name,interviewers_department)
values(?,?,?,?,?)
''', (interview2.candidate_name,
      interview2.role_applied_for,
      interview2.interview_date_time,
      interview2.interviewers_name,
      interview2.interviewers_department))

print("\nInterview 1:")
print(interview1.call_display())

print("\nInterview 2:")
print(interview2.call_display())

with open("records.log", "w") as wopj:
    wopj.write("Courier Records:\n")
    wopj.write(courier1.display())
    wopj.write(courier2.display())
    wopj.write("\nVisitor Records:\n")
    wopj.write(visitor1.visitor_display())
    wopj.write(visitor2.visitor_display())
    wopj.write("\nInterview Records:\n")
    wopj.write(interview1.call_display())
    wopj.write(interview2.call_display())

print("Records have been written to 'records.log'")

conn.commit()
conn.close()
