# This class represents an enrollment with attributes for student, course, and grade, and methods to get enrollment information,
#  add a grade, and convert the enrollment information to CSV format.

class Enrollment:
        def __init__(self, student, course, grade):
            ''' Define the class'''
            self.student = student
            self.course = course
            self.grade = grade

        def get_info(self):
            '''Returns all enrollment informations.'''
            return f"Student: {self.student}, Course: {self.course}, Grade: {self.grade}"
        
        def add_grade(self, grade):
            '''assigns a grade to the student in a specific course.'''
            self.grade = grade
            
        def to_csv(self):
            '''Returns enrollment informations in csv format.'''
            return f"{self.student.to_csv()},{self.course.to_csv()},{self.grade}"