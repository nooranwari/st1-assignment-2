from enum import Enum
from typing import Optional


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"


class InvalidStatusTransitionError(Exception):
    pass


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        patient: Patient,
        practitioner: Practitioner,
        date: str,
        time: str
    ):
        if not appointment_id.strip():
            raise ValueError("Appointment ID is required")

        if not isinstance(patient, Patient):
            raise ValueError("A valid patient is required")

        if not isinstance(practitioner, Practitioner):
            raise ValueError("A valid practitioner is required")

        if not date.strip():
            raise ValueError("Date is required")

        if not time.strip():
            raise ValueError("Time is required")

        self._appointment_id = appointment_id
        self._patient = patient
        self._practitioner = practitioner
        self._date = date
        self._time = time
        self._status = AppointmentStatus.SCHEDULED

    def get_status(self) -> AppointmentStatus:
        return self._status

    def update_details(
        self,
        date: Optional[str] = None,
        time: Optional[str] = None,
        practitioner: Optional[Practitioner] = None
    ) -> None:

        if self._status == AppointmentStatus.CANCELLED:
            raise ValueError("Cancelled appointments cannot be updated")

        if date is not None:
            if not date.strip():
                raise ValueError("Date is required")
            self._date = date

        if time is not None:
            if not time.strip():
                raise ValueError("Time is required")
            self._time = time

        if practitioner is not None:
            if not isinstance(practitioner, Practitioner):
                raise ValueError("A valid practitioner is required")
            self._practitioner = practitioner

    def cancel(self) -> None:
        if self._status == AppointmentStatus.CANCELLED:
            raise InvalidStatusTransitionError(
                "Appointment is already cancelled"
            )

        self._status = AppointmentStatus.CANCELLED

    def check_clash(self, other: "Appointment") -> bool:
        return (
            self._practitioner.get_practitioner_id()
            == other._practitioner.get_practitioner_id()
            and self._date == other._date
            and self._time == other._time
            and self._status == AppointmentStatus.SCHEDULED
            and other._status == AppointmentStatus.SCHEDULED
        )
    