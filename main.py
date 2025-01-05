#!/usr/bin/env python3

from classes import Student, Teacher, Courses
from utilities import Student_Database, teacher_database, AlgoMenus
from formulas import SortingAlgorithms, SearchingAlgorithms


def main():
    student_database = Student_Database()
    students = student_db.txt_to_csv()

    teacher_file_name = "teachers.csv"
    teacher_file_size = 500
    teacher_utilities = teacher_database()
    teachers = teacher_utilities.teacher_data_file(teacher_file_name, teacher_file_size)

    while True:
        print("\n1. Student")
        print("2. Teacher")
        print("3. Courses")
        print("\nType EXIT to quit this application")

        select = input("\nPlease select your choice: ").lower()

        if select == "exit":
            break
        elif select == "1":
            second_menu()
        elif select == "2":
            third_menu()
        elif select == "3":
            fourth_menu()

def second_menu():

    while True:
        print("\nMAIN MENU")
        print("1. ADD NEW STUDENT")
        print("2. DELETE STUDENT")
        print("3. SHOW STUDENTS")
        print("4. SEARCH STUDENT")
        print("\nType EXIT to quit this menu")

        student_choice = input("\nPlease choose a number: ").lower()


        if student_choice == "exit":
            break
        elif student_choice == "1":
            add_new_student_menu(student_db)
        elif student_choice == "2":
            delete_student_menu(student_db)
        elif student_choice == "3":
            show_students_menu(student_db)
        elif student_choice == "4":
            search_student_menu(student_db)
        else:
            print("Invalid choice. Please try again.")

def third_menu():
    
    while True:
        print("\nMAIN MENU")
        print("1. ADD NEW TEACHER")
        print("2. DELETE TEACHER")
        print("3. SHOW TEACHER LIST")
        print("4. SEARCH FOR TEACHER")
        print("\nType EXIT to quit this menu")
        
        teacher_choice = input("\nPlease choose a number: ").lower()

        if teacher_choice == "exit":
            break
        elif teacher_choice == "1":
            teacher = Teacher()
            teacher.teacher_add_info()
        elif teacher_choice == "2":
            teacher = Teacher()
            teacher.teacher_delete_info()
        elif teacher_choice == "3":
            teacher = Teacher()
            teacher.show_search_data()
        elif teacher_choice == "4":
            teacher = Teacher()
            teacher.show_search_data()    

def fourth_menu():

    while True:
        print("\nCourses")
        print("1. Data Structures and Algorithms")
        print("2. Web Development")
        print("3. Mobile Development")
        print("\nType EXIT to quit this menu")
        
        choice = input("\nPlease choose a number: ")

        if choice == "exit":
            break
        elif choice == "1":
            course = Courses()
            course.data_structures()
        elif choice == "2":
            course = Courses()
            course.web_dev()
        elif choice == "3":
            course = Courses()
            course.mobile_dev()


def add_new_student_menu(student_db):
    print("\n*******************\nSTUDENT ADD MENU\n*******************")
    print("Enter the student details")
    firstname = input("Enter First Name: ")
    lastname = input("Enter Last Name: ")
    email = input("Enter Email Address: ")
    campus = input("Campus (Auckland, Hamilton, Wellington, Christchurch, and Dunedin): ")

    new_student = Student(firstname, lastname, email, campus)
    student_db.add_new_student(new_student)

    print("\n*** Record Successfully added. ***")

def delete_student_menu(student_db):
    print("\n*******************\nDELETE STUDENT MENU\n*******************")
    student_id = int(input("Enter student ID (ranges from 100-600) to delete the record: "))
    
    student_db.delete_student(student_id)

def show_students_menu(student_db):
    while True:
        print("\n*******************\nSTUDENTS SHOW MENU\n*******************")
        print("\n1. SHOW ALL STUDENTS BY ID")
        print("2. SHOW ALL STUDENTS BY FIRST NAME (ASCENDING ORDER)")
        print("3. SHOW ALL STUDENTS BY LAST NAME (ASCENDING ORDER)")
        print("4. SHOW ALL STUDENTS BY CAMPUS (ASCENDING ORDER)")
        print("\nType EXIT to quit this menu")
        
        choice = input("\nPlease select your choice: ")

        if choice.lower() == "exit":
            break
        elif choice == '1':
            sorted_students = SortingAlgorithms.bubble_sort(student_db.students, 'id', 'ascending')
            for student in sorted_students:
                print(f"ID: {student.id}, Name: {student.firstname} {student.lastname}, Email: {student.email}, Campus: {student.campus}")
        elif choice == '2':
            sorted_students = SortingAlgorithms.quick_sort(student_db.students, 'firstname', 'ascending')
            for student in sorted_students:
                print(f"ID: {student.id}, Name: {student.firstname} {student.lastname}, Email: {student.email}, Campus: {student.campus}")
        elif choice == '3':
            sorted_students = SortingAlgorithms.quick_sort(student_db.students, 'lastname', 'ascending')
            for student in sorted_students:
                print(f"ID: {student.id}, Name: {student.firstname} {student.lastname}, Email: {student.email}, Campus: {student.campus}")
        elif choice == '4':
            sorted_students = SortingAlgorithms.quick_sort(student_db.students, 'campus', 'ascending')
            for student in sorted_students:
                print(f"ID: {student.id}, Name: {student.firstname} {student.lastname}, Email: {student.email}, Campus: {student.campus}")
        else:
            print("Invalid choice. Please try again.")

def search_student_menu(student_db):
    while True:
        print("\n*******************\nSTUDENT SEARCH MENU\n*******************")
        print("\n1. SEARCH STUDENT BY ID")
        print("2. SEARCH STUDENT BY FIRST NAME")
        print("3. SEARCH STUDENT BY LAST NAME")
        print("\nType EXIT to quit this menu")

        choice = input("\nPlease select you choice: ")

        if choice == "exit":
            break
        elif choice == '1':
            search_by = 'id'
        elif choice == '2':
            search_by = 'firstname'
        elif choice == '3':
            search_by = 'lastname'
        else:
            print("Invalid choice. Please try again.")
            return

        search_value = input(f"Enter the {search_by} to search: ")
        student_db.search_student(search_by, search_value)
  

if __name__ == "__main__":
    student_db = Student_Database()
    students = student_db.txt_to_csv()
    print("\n**** Welcome TO WHITECLIFFE College of Information Technology ***")
    print("******************** STUDENT PORTAL *************************")
    print("CSV file 'student_data.csv' successfully loaded")
    
    sorted_students, sorting_time = student_db.generate_measurement(
        SortingAlgorithms.quick_sort, student_db.students, bubble_list="id", sorting_order="ascending"
    )
    print(f"Sorting Time: {sorting_time} seconds")

    searched_students, searching_time = student_db.generate_measurement(
        SearchingAlgorithms.linear_search, student_db.students, bubble_list="id", value="some_value"
    )
    print(f"Searching Time: {searching_time} seconds")

    main()
