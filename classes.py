#!/usr/bin/env python3

import random
from faker import Faker

# Students

class Student:
    def __init__(self, id="", firstname="", lastname="", email="", campus=""):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.campus = campus
        self.id = id 


# Teachers

class Teacher:
    def __init__(self, firstname="", lastname="", qualification="", age="", campus="", email="", id=""):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.campus = campus
        self.qualification = qualification
        self.email = email
        self.id = id

    def teacher_add_info(self):
        print("\n*******************\nTEACHER ADD MENU\n*******************")
        print("\nEnter the following information for the new teacher: ")
        self.firstname = input('First name: ')
        self.lastname = input('Last name: ')
        self.age = int(input('Age: '))
        self.campus = input("Campus (one of Auckland, Hamilton, Wellington, Christchurch, and Dunedin): ")
        self.qualification = input('Qualification (PhD, Master, Bachelor, Diploma): ')
        print(f"\nNew teacher ({self.firstname}) ({self.lastname}) ({self.age}) ({self.campus}) ({self.qualification}) has been added to the system.")
        self.email_generate()
        self.id_generate()

    def teacher_delete_info(self):
        print("\n*******************\nDELETE TEACHER MENU\n*******************")
        teacher_id = input("\nEnter teacher ID to delete the record: ")
        print(f"\n**** Teacher with ID ({teacher_id}) is deleted from the system.")


    def show_search_data(self):
        while True:
            print("1. First Name")
            print("2. Last Name")
            print("3. Age")
            print("4. Campus")
            print("5. Qualification")
            print("6. Email")
            print("7. ID")
            print("8. To exit this menu")
            choice = int(input("\nPlease choose a number: "))
            if choice == "8":
                break
            else:
                return choice

    def generate_data(self):
        self.firstname_generate()
        self.lastname_generate()
        self.qualification_generate()
        self.age_generate()
        self.campus_generate()
        self.email_generate()
        self.id_generate()

    def firstname_generate(self):
        fake = Faker()
        self.firstname = fake.first_name()

    def lastname_generate(self):
        fake = Faker()
        self.lastname = fake.last_name()

    def qualification_generate(self):
        qualifications = ['PhD', 'Master', 'Bachelor', 'Diploma']
        qual_probabilities = [0.3, 0.7, 0.3, 0.4]

        qual_weights = [prob / sum(qual_probabilities) for prob in qual_probabilities]
        self.campus = random.choices(qualifications, weights=qual_weights)[0]

    def age_generate(self):
        age_ranges = [(20, 30), (30, 50), (50, 65)]
        age_probabilities = [0.3, 0.6, 0.1]

        age_weights = [prob / sum(age_probabilities) for prob in age_probabilities]

        random_range = random.choices(age_ranges, weights=age_weights)[0]
        self.age = random.randint(*random_range)

    def campus_generate(self):
        campuses = ['Auckland', 'Hamilton', 'Wellington', 'Christchurch', 'Dunedin']
        campus_probabilities = [0.3, 0.2, 0.2, 0.2, 0.1]

        campus_weights = [prob / sum(campus_probabilities) for prob in campus_probabilities]
        self.campus = random.choices(campuses, weights=campus_weights)[0]

    def email_generate(self):
        self.email = self.firstname + '.' + self.lastname + '@lecturer.whitecliffe.ac.nz'

    def id_generate(self):
        self.id = self.firstname[:3] + self.lastname[:3] + '_WHITECLIFFE'

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(
            self.firstname,
            self.lastname,
            self.qualification,
            self.age,
            self.email,
            self.campus,
            self.id,
        )

        
# Courses

class Courses:
    def data_structures(self):
        select_data = input("Would you like to enroll to this course (Y, N): ")
        if select_data == "Y":
            print("\nCourse added to the system.")
        else:
            print("\nThanks")
        return select_data

    def web_dev(self):
        select_web = input("Would you like to enroll to this course (Y, N): ")
        if select_web == "Y":
            print("\nCourse added to the system.")
        else:
            print("\nThanks")
        return select_web

    def mobile_dev(self):
        select_mobile = input("Would you like to enroll to this course (Y, N): ")
        if select_mobile == "Y":
            print("\nCourse added to the system.")
        else:
            print("\nThanks")
        return select_mobile
    