class Patient:
    def __init__(self, patient_id: str, name: str):
        if not isinstance(patient_id, str) or not patient_id.strip():
            raise ValueError("Patient ID is required")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Patient name is required")

        self._patient_id = patient_id
        self._name = name

    def get_patient_id(self) -> str:
        return self._patient_id

    def get_name(self) -> str:
        return self._name

    def update_name(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Patient name is required")

        self._name = name