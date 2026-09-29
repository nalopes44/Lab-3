class PatientExam:

    def __init__(self, exam_id: int, date: str, name: str, weight: int, height: float):
        self.id = exam_id
        self.exam_date = date
        self.full_name = name
        self.weight_kg = weight
        self.height_m = height

    def get_BMI(self) -> float:
        return self.weight_kg / self.height_m ** 2

    def get_exam_month(self) -> int:
        return self.exam_date.split('/')[0]
