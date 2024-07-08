import datetime

class Appointment:
    def _init_(self, patient_name, doctor_name, appointment_date):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.appointment_date = appointment_date

    def _str_(self):
        return f"Appointment Details:\nPatient Name: {self.patient_name}\nDoctor Name: {self.doctor_name}\nAppointment Date: {self.appointment_date}"

class Scheduler:
    def _init_(self):
        self.appointments = []

    def schedule_appointment(self):
        patient_name = input("Enter patient name: ")
        doctor_name = input("Enter doctor name: ")

        # Get current date and time from the device
        current_datetime = datetime.datetime.now()
        appointment = Appointment(patient_name, doctor_name, current_datetime)
        self.appointments.append(appointment)

    def get_appointments(self):
        if not self.appointments:
            return[]
        return self.appointments

    def get_appointments_by_date(self, date):
        appointments_by_date = []
        for appointment in self.appointments:
            if appointment.appointment_date.date() == date.date():
                appointments_by_date.append(appointment)
        return appointments_by_date

scheduler = Scheduler()

# Schedule appointments using user input
scheduler.schedule_appointment()
scheduler.schedule_appointment()
scheduler.schedule_appointment()

# Get all appointments
all_appointments = scheduler.get_appointments()
if not all_appointments:
    print("No Appointments Scheduled")
else:
    for appointment in all_appointments:
        print(appointment)

# Get appointments by date
appointments_by_date = scheduler.get_appointments_by_date(datetime.datetime.now())
if not appointments_by_date:
    print("No Appointments Scheduled Today")
else:  
    for appointment in appointments_by_date:
        print(appointment)