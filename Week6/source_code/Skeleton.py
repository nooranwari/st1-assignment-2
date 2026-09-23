class Patient:
    def __init__(self, patient_id, details):
        self.patient_id = patient_id
        self.details = details

    def update_details(self):
        pass

    def view_appointment_history(self):
        pass


class Practitioner:
    def __init__(self, practitioner_id, details, availability):
        self.practitioner_id = practitioner_id
        self.details = details
        self.availability = availability

    def update_details(self):
        pass

    def update_availability(self):
        pass


class Appointment:
    def __init__(self, appointment_id, patient, practitioner, date, time, status):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date = date
        self.time = time
        self.status = status

    def update_details(self):
        pass

    def cancel(self):
        pass

    def check_clash(self):
        pass