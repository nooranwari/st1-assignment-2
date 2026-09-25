class Practitioner:
    def __init__(
        self,
        practitioner_id: str,
        name: str,
        specialty: str,
        availability: list[str]
    ):
        if not practitioner_id.strip():
            raise ValueError("Practitioner ID is required")

        if not name.strip():
            raise ValueError("Practitioner name is required")

        if not specialty.strip():
            raise ValueError("Specialty is required")

        if not isinstance(availability, list):
            raise ValueError("Availability must be a list")

        self._practitioner_id = practitioner_id
        self._name = name
        self._specialty = specialty
        self._availability = availability

    def get_practitioner_id(self) -> str:
        return self._practitioner_id

    def get_name(self) -> str:
        return self._name

    def get_specialty(self) -> str:
        return self._specialty

    def get_availability(self) -> list[str]:
        return list(self._availability)

    def update_specialty(self, specialty: str) -> None:
        if not specialty.strip():
            raise ValueError("Specialty is required")

        self._specialty = specialty

    def update_availability(self, availability: list[str]) -> None:
        if not isinstance(availability, list):
            raise ValueError("Availability must be a list")

        self._availability = availability


