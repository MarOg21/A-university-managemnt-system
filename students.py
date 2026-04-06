## This class represents a student with attributes for name and student ID, and methods to get information, 
# update the name, and convert the student's information to CSV format.
class Students:
    def __init__(self, name, student_id):
        ''' Defines the class'''
        self.name = name
        self.student_id = student_id

    def get_info(self):
        '''Returns students informations.'''
        return f"Name: {self.name}, Student ID: {self.student_id}"
    
    def get_id(self):
        '''Returns the student ID.'''
        return self.student_id
    
    def update_name(self, N_name):
        '''Updates the student's name if need be.'''
        self.name = N_name

    def to_csv(self):
        '''Returns students information in a simple  CSV format.'''
        return f"{self.name},{self.student_id}"