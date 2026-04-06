from department import Course, Department
from students import Students
dept_obj = Department()

# This is the main interface of the program where the user can interact with the department, add students and courses, enroll students in courses, 
# and save or load data. The user is prompted to enter information about students and courses, and then given options to enroll students, show students, save data, and load data.

name = input(" Enter name of the student: ")
student_id = input(" Enter the student ID: ")

s1 = Students(name, student_id)
dept_obj.add_student(s1)

course_name = input(" Enter course name: ")
course_code = input(" Enter course code: ")
credits = int(input(" Enter course credits: "))

c1 = Course(course_name, course_code, credits)
dept_obj.add_course(c1)

choice = input(" Do you want to enroll the student in the course? ")
choices = ['yes', 'cancel']

if choice == 'yes':
    dept_obj.add_student(s1)
    print(f"{s1.name} has been enrolled")
else:    
    print(f"{s1.name} Action has been canceled")

# show students
print("\nStudents in the department:")
dept_obj.show_students()

#save data
save = input(" Do you want the data to be saved?")
choices = ['yes', 'no']
if save == 'yes':
    dept_obj.save_students()
    print("Data has been saved successfully")
else:
    print("Data has not been saved")

    # load data
load = input(" Do you want to load the data?" )
choices = ['yes', 'no']
if load == 'yes':
    dept_obj.load_students()
    print("Data has been loaded successfully")

    print("\nStudents in the department:")
    dept_obj.show_students()
else:
    print("Data has not been loaded")