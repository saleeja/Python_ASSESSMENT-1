class Student:
    def __init__(self, name, height):
        # Initialize Student object with name and height
        self.name = name
        self.height = height

class SchoolHeightRecord:
    def __init__(self):
        # Initialize SchoolHeightRecord object with an empty list for students
        self.students = []

    def add_student(self, student):
        # Add a student to the list of students
        self.students.append(student)

    def display_records(self):
        # Display the school's height records
        print("School Height Records:")
        for student in self.students:
            print(f"{student.name}: {student.height} cm")

    def calculate_average_height(self):
        # Calculate and display the average height of all students
        if not self.students:
            print("No student records available.")
            return
        total_height = sum(student.height for student in self.students)
        average_height = total_height / len(self.students)
        print(f"Average Height: {average_height:.2f} cm")

    def display_max_min_height_students(self):
        # Identify and display students with the maximum and minimum heights
        if not self.students:
            print("No student records available.")
            return
        max_height_student = max(self.students, key=lambda x: x.height)
        min_height_student = min(self.students, key=lambda x: x.height)

        print(f"Student with Maximum Height: {max_height_student.name} ({max_height_student.height} cm)")
        print(f"Student with Minimum Height: {min_height_student.name} ({min_height_student.height} cm)")

# Function to get user input for student details
def get_student_details():
    try:
        name = input("Enter student name: ")
        height = float(input("Enter student height (in cm): "))
        return Student(name, height)
    except ValueError:
        print("Invalid input. Please enter a valid number for height.")
        return None


school_records = SchoolHeightRecord()

# Get user input for student records
while True:
    add_more = input("Do you want to add a student record? (yes/no): ").lower()
    if add_more != 'yes':
        break
    student = get_student_details()
    if student:
        school_records.add_student(student)

# Displaying records
school_records.display_records()
school_records.calculate_average_height()
school_records.display_max_min_height_students()


