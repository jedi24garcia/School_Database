import os
import csv
import pandas
from classes import Teacher, Student
import time

# Students Database

class Student_Database:
    def __init__(self):
        self.students = []

    def generate_id(self, firstname, lastname):
        return f"{firstname[:3]}{lastname[:3]}{str(2023)[-2:]}"

    def generate_measurement(self, function, *args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        execute = end - start
        return result, execute

    def add_new_student(self, student):
        self.students.append(student)

    def delete_student(self, student_id):
        if student_id in range(100, 601):
            print(f"\n**** Student with ID ({student_id}) is deleted from the system.")
        else:
            print("No student found.")

    def search_student(self, search_by, value):
        result_students = [s for s in self.students if getattr(s, search_by) == value]
        for student in result_students:
            print(f"ID: {student.id}, Name: {student.firstname} {student.lastname}, Email: {student.email}, Campus: {student.campus}")

    def txt_to_csv(self, csv_filename='student_data.csv'):
        students = []
        with open('student_data.txt', mode="r", newline="") as txt_file:
            lines = txt_file.readlines()

        with open(csv_filename, mode="w", newline="") as csv_file:
            fieldnames = ['First Name', 'Last Name', 'Email', 'Campus', 'ID']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')

            writer.writeheader()

            for line in lines:
                data = line.strip().split('\t')
                if len(data) >= 5:
                    writer.writerow({
                        'First Name': data[0],
                        'Last Name': data[1],
                        'Email': data[2],
                        'Campus': data[3],
                        'ID': data[4],
                    })
                    student = Student(
                        firstname=data[0],
                        lastname=data[1],
                        email=data[2],
                        campus=data[3],
                        id=data[4]
                    )
                    students.append(student)

        self.students = students
        print(f"CSV file '{csv_filename}' successfully generated.")
        return students



# Teachers Database

class teacher_database:
    def file_exists(self,file_name):
        if os.path.isfile(file_name):
            return True
        else:
            return False

    def teacher_data_file(self, file_name, file_size):
        if not self.file_exists(file_name):
            print('File does not exist. Generating a new one now.')
            teachers = self.generate_teacher_data_file(file_name, file_size)
            print('The file has been successfully generated.')
        else:
            print('File already exists.')
            teachers = self.read_teacher_data_file(file_name)

        return teachers

    def generate_teacher_data_file(self,file_name,file_size):
        teachers = []
        for i in range(file_size):
            teacher = Teacher()
            teacher.generate_data()
            teachers.append(teacher)

        df = pandas.DataFrame([t.__dict__ for t in teachers])

        df.to_csv(file_name, index=False)

        return teachers

    def read_teacher_data_file(self,file_name):
        df = pandas.read_csv(file_name)

        teachers = []
        for i in range(len(df)):
            teacher = Teacher()
            teacher.__dict__ = df.iloc[i].to_dict()
            teachers.append(teacher)

        return teachers

    def save_teacher_data_file(self,file_name,teachers):
        df = pandas.DataFrame([t.__dict__ for t in teachers])

        df.to_csv(file_name, index=False)


class AlgoMenus:

    def sort_menu(self):
        print("1. Ascending")
        print("2. Descending(Optional)")
        choice = int(input("Please select: "))
        return choice

    def search_formula(self):
        print("1. Linear Search")
        print("2. Binary Search")
        choice = int(input("Please select: "))
        return choice         

    def formula_menu(self):
        print("1. Bubble Sort")
        print("2. Quick Sort")
        choice = int(input("Please select: "))
        return choice