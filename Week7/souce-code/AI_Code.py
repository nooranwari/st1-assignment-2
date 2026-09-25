from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


@dataclass
class Appointment:
    appointment_id: str
    patient_id: str
    practitioner_id: str
    date: str          # e.g. "2026-09-24"
    time: str          # e.g. "10:30"
    status: AppointmentStatus = AppointmentStatus.SCHEDULED

    def update_details(
        self,
        date: Optional[str] = None,
        time: Optional[str] = None,
        practitioner_id: Optional[str] = None
    ) -> None:
        """
        Update appointment details.
        FR-09: Allows updating appointment details.
        Protects cancelled appointments from being edited.
        """

        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("Cancelled appointments cannot be modified.")

        if date:
            self.date = date
        if time:
            self.time = time
        if practitioner_id:
            self.practitioner_id = practitioner_id

    def cancel(self) -> None:
        """
        Cancel the appointment.
        FR-10: Cancel an appointment.
        Cancelled appointments remain as objects (per your instruction).
        """

        if self.status == AppointmentStatus.CANCELLED:
            return  # Already cancelled; silently ignore.

        self.status = AppointmentStatus.CANCELLED

    def check_clash(self, other: Appointment) -> bool:
        """
        Check if this appointment clashes with another appointment.
        FR-08: Prevent double-booking of the same practitioner.
        """

        same_practitioner = self.practitioner_id == other.practitioner_id
        same_date = self.date == other.date
        same_time = self.time == other.time

        return same_practitioner and same_date and same_time

print("Starting manual tests")

# Test 1: Create a valid appointment
appointment = Appointment(
    "A001",
    "P001",
    "PR001",
    "2026-09-24",
    "10:30"
)

print("Test 1: Valid appointment created - Passed")


# Test 2: Test invalid input
invalid_appointment = Appointment(
    "",
    "",
    "",
    "",
    ""
)

if invalid_appointment.appointment_id == "":
    print("Test 2: Blank appointment ID was accepted - Failed")
else:
    print("Test 2: Invalid input was rejected - Passed")


# Test 3: Cancel a scheduled appointment
appointment.cancel()

if appointment.status == AppointmentStatus.CANCELLED:
    print("Test 3: Appointment cancelled - Passed")
else:
    print("Test 3: Appointment was not cancelled - Failed")


# Test 4: Cancel the same appointment again
try:
    appointment.cancel()
    print("Test 4: Second cancellation was silently ignored - Failed")
except Exception as error:
    print("Test 4: Second cancellation raised an error - Passed")
    print(error)