# This class represents a course with attributes for course name, course code, and credits, and methods to get information,
#  update the course name, add or remove students, and convert the course information to CSV format.
class Course:
    def __init__(self, course_name, course_code, credits):
        ''' Defines the class'''
        self.course_name = course_name
        self.course_code = course_code
        self.credits = credits

    def get_info(self):
        '''Returns the course informations.'''
        return f"Course Name: {self.course_name}, Course Code: {self.course_code}, Credits: {self.credits}"

    def get_code(self):
        '''Returns the course code.'''
        return self.course_code

    def get_credits(self):
        '''Returns the course credits.'''
        return self.credits

    def update_course_name(self, N_course_name):
        '''Updates the course name incase of any changes.'''
        self.course_name = N_course_name

    def add_student(self, student):
        '''Adds a student to a specific course.'''
        self.students = []
        '''creates an empty list to store students in the course'''
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        '''Removes a student from a specific course.'''
        if student in self.students:
            self.students.remove(student)

    def to_csv(self):
        '''Returns course informations in a simple csv format.'''
        return f"{self.course_name},{self.course_code},{self.credits}"