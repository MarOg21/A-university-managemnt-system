from students import Students
from course import Course
from enrollment import Enrollment

# This class represents a department with attributes for courses and students, and methods to add or remove courses 
# and students, show students, enroll students in courses, and save or load student information to/from a CSV file.

class Department:
    def __init__(self):
        self.courses = []
        self.students = []
        '''creates empty lists to store courses and students in the department'''

    def add_course(self, course):
        '''Adds a course to the department.'''
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        '''Removes a course from the department.'''
        if course in self.courses:
            self.courses.remove(course)

    def add_student(self, student):
        '''Adds a student to the department.'''
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        '''Removes a student from the department.'''
        if student in self.students:
            self.students.remove(student)

    def show_students(self):
        '''Displays all students in the department.'''
        for s in self.students:
            print(f"Name: {s.name}, ID: {s.student_id}")

    def enroll(self, student, course):
        '''Enrolls a student in a course.'''
        student = None
        course = None
        '''checks if the student exists in the department before enrolling.'''
        for S in self.students:
            if S == student:
                student = S
        '''checks if the course exists in the department before enrolling.n '''
        for c   in self.courses:
            if c == course:
                course = c
        if student and course:
            course.add_student(student)
            print(f"{student.name} has been enrolled in {course.course_name}.")
        else:
            print("Student or course not found in the department.")

    def save_students(self):
        '''Saves the students information to a CSV file.'''
        try: 
            with open('dept_data.csv', 'w') as file:
                for student in self.students:
                    '''this goes through every student in the list''' 
                    file.write(student.to_csv() + '\n')
        except Exception as e:
            print(f"an error has occurred: {e}")

    def load_students(self):
        '''Loads students information from a CSV file.'''
        self.students = []  # This Clears the existing list before loading new data
        try:
            with open('dept_data.csv', 'r') as file:
                for line in file:
                    '''this goes through every line in the file'''
                    name, student_id = line.strip().split(',')
                    student = Students(name, student_id)
                    self.students.append(student)
        except FileNotFoundError:
            print("student file not found")

        