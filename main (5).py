'''
Unit 3: Challenge 3.2- Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.
'''
class student:

    def __init__(self,name,rollno,cgpa):
        self.name=name
        self.rollno=rollno
        self.cgpa=cgpa

def sort_students(student_list):
    sorted_students=sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

students=[
    student("Jasmine","A123",8.2),
    student("Lily","A124",9.2),
    student("Lotus","A125",7.9),
    student("Rose","A126",8.8),]

sorted_students=sort_students(students)

for student in sorted_students:
    print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.rollno,student.cgpa))