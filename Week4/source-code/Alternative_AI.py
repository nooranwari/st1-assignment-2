appointments = []   # simple in‑memory list

def add_appointment(patient_name, practitioner_name, appointment_time):
    """Store a basic appointment using simple Python data structures.
       No database, no GUI — just a list of dictionaries.
    """

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)
    return "Appointment stored."