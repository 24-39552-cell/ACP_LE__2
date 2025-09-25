# Define a Student class to represent each student
class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id_name = (str(student_id), student_name) # store ID as string
        self.email = email
        self.grades = grades if grades is not None else {} # default to empty dict
        self.courses = courses if courses is not None else set() # default to empty set

# String Representation
    def __str__(self):
        return (f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, "f"Email: {self.email}, Grades: {self.grades}, "f"Courses: {list(self.courses)}") # convert set to list for display

    # Method to calculate GPA from grades
    def calculate_gpa(self):
        if not self.grades: # if no grades exist, return a message
            return "No grades available." 

        # Convert scores to GPA
        gpa_values = []
        for score in self.grades.values():
            if score >= 90: gpa_values.append(4.0) 
            elif score >= 80: gpa_values.append(3.0)
            elif score >= 70: gpa_values.append(2.0)
            elif score >= 60: gpa_values.append(1.0)
            else: gpa_values.append(0.0)

        gpa = round(sum(gpa_values) / len(gpa_values), 2)

        # Convert GPA to letter grade
        if gpa >= 3.7: grade = "A" 
        elif gpa >= 3.0: grade = "B"
        elif gpa >= 2.0: grade = "C"
        elif gpa >= 1.0: grade = "D"
        else: grade = "F"
        # Return GPA and letter grade
        return f"GPA: {gpa}, Grade: {grade}"

# Define a StudentRecords class to manage multiple students
class StudentRecords:
    def __init__(self):
        self.students = [] # list to hold Student objects

    # Add Student
    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        student_id = str(student_id)
        # create and add new student
        new_student = Student(student_id, student_name, email, grades, courses)
        self.students.append(new_student) # add to list
        return "Student added successfully" 

     # Updating Info for Student
    def update_student(self, student_id, email=None, grades=None, courses=None): 
        student_id = str(student_id) 
        for student in self.students: 
            if student.id_name[0] == student_id: 
                if email:
                    student.email = email
                if grades:
                    student.grades.update(grades)
                if courses:
                    student.courses.update(courses)
                return "Student updated successfully" 
        return "Student not found"

    # Delete Student using the remove() method
    def delete_student(self, student_id):
        student_id = str(student_id) 
        for student in self.students: 
            if student.id_name[0] == student_id:
                self.students.remove(student) # remove student from list
                return "Student deleted successfully"
        return "Student not found"

    # Enroll in a Course
    def enroll_course(self, student_id, course):
        student_id = str(student_id)
        for student in self.students:
            if student.id_name[0] == student_id:
                # check for duplicate course
                if course in student.courses:
                    return f"{student.id_name[1]} is already enrolled in {course}" 
                else: 
                    student.courses.add(course) # add course
                    return f"{student.id_name[1]} enrolled in {course}" 
        return "Student not found" # if student ID not found

    # Search Student by ID
    def search_student(self, student_id):
        student_id = str(student_id)
        for student in self.students: 
            if student.id_name[0] == student_id: 
                return str(student) 
        return "Student not found" # if not found, return message

    # Search by Name 
    def search_by_name(self, name):
        matches = [str(student) for student in self.students
                   if name.lower() in student.id_name[1].lower()]
        return "\n".join(matches) if matches else "No students found"
    # joins all matching students into a one string

    # Show All Students
    def show_all(self):
        if not self.students: # if list is empty
            return "No students available."
        return "\n".join(str(s) for s in self.students) # join all students into one string

# EXAMPLE USAGE AND TESTING

record = StudentRecords() # create an instance of StudentRecords

# Add student infos
print("Adding students:") 
print(record.add_student("24-39552", "Venn", "venn@example.com", {"Math": 90}, {"Math"}))
print(record.add_student("25-67898", "Josh", "josh@example.com", {"Science": 85}, {"Science"}))

# Show all students
print("\nAll Students:")
print(record.show_all()) 

# Update student info
print("\nUpdating Info for Student ID: 24-39552")
print(record.update_student("24-39552", email="update@example.com", grades={"Math": 75, "English": 80}, courses={"English"}))
print(record.show_all()) # show updated info

# Delete a student
print("\nDelete Student:")
print(record.delete_student("25-67898")) # delete Josh
print(record.delete_student("26-72646")) # not found
print(record.show_all())

# Enroll in a course
print("\nEnroll in Course:")
print(record.enroll_course("25-67898", "Math"))      # not found (Josh deleted)
print(record.enroll_course("24-39552", "Science"))   # add new course
print(record.enroll_course("24-39552", "Math"))      # duplicate course
print(record.show_all())

# Search Student by ID
print("\nSearch by ID:")
print(record.search_student("24-39552")) 
print(record.search_student("26-72646"))  # no match

# Search by Name
print("\nSearch by Name:")
print(record.search_by_name("Venn")) 
print(record.search_by_name("VennMercado"))  # no match

# Get GPA
print("\nGetting the student GPA:")
for student in record.students: 
    print(f"{student.id_name[1]}'s GPA: {student.calculate_gpa()}") # calculate and display GPA


            
