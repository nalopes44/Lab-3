import csv
import calendar
from collections import Counter
from classes import PatientExam

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

    avg_bmi = sum(exam.get_BMI() for exam in exams) / len(exams) 
    busiest_month = calendar.month_name[Counter([exam.get_exam_month() for exam in exams]).most_common(1)[0][0]]
main()
