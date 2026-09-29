import csv
from classes import PatientExam
# your code here

def main():
    exams = []

    with (open("patient_data.csv", "r", newline="") as patient_data):
        reader = csv.reader(patient_data)

        #skip header row
        next(reader)

        for row in reader:
            exam = PatientExam(exam_id=int(row[0]), 
                               date=row[1],
                               name=row[2].strip(),
                               weight=int(row[3]),
                               height=float(row[4])
                               )
            exams.append(exam)