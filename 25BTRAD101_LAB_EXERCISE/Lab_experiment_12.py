import csv
import os
FILENAME = "students.txt"
# Read student records from file
def load_students():
students = []
if os.path.exists(FILENAME):
with open(FILENAME, "r", newline=
reader = csv.DictReader(file)
students = list(reader)
return students
"") as file:
# Save records into file
def save_students(students):
with open(FILENAME, "w", newline=
"") as file:
fields = ["USN", "Name", "Department", "Marks"]
writer = csv.DictWriter(file, fieldnames=fields)
writer.writeheader()
writer.writerows(students)
# Add a new student
def add_student():
students = load_students()
usn = input("Enter USN: ").strip()
if not usn:
return
print("USN cannot be empty!")
for student in students:
if student["USN"] == usn:
print("Student already exists!")
return
name = input("Enter student name: ").strip()
department = input("Enter department: ").strip()
if not name or not department:
print("Name and department cannot be empty!")
return
try:
marks = float(input("Enter marks (0-100): "))
if marks < 0 or marks > 100:
print("Marks must be between 0 and 100!")
return
except ValueError:
return
print("Please enter valid numeric marks!")
student = {
"USN": usn,
"Name": name,
"Department": department,
"Marks": marks
}
students.append(student)
save_students(students)
print("Student record added successfully!")
# Display all student records
def display_students():
students = load_students()
if not students:
return
print("No student records found!")
print("\n===== STUDENT RECORDS =====")
for student in students:
print("\nUSN:", student["USN"])
print("Name:", student["Name"])
print("Department:", student["Department"])
print("Marks:", student["Marks"])
# Search for a student
def search_student():
students = load_students()
usn = input("Enter USN to search: ").strip()
for student in students:
if student["USN"] == usn:
print("\nStudent Found!")
print("USN:", student["USN"])
print("Name:", student["Name"])
print("Department:", student["Department"])
print("Marks:", student["Marks"])
return
print("Student not found!")
# Update student details
def update_student():
students = load_students()
usn = input("Enter USN to update: ").strip()
for student in students:
if student["USN"] == usn:
print("Leave a field blank to keep its old value.")
name = input("Enter new name: ").strip()
department = input("Enter new department: ").strip()
marks_input = input("Enter new marks: ").strip()
if name:
student["Name"] = name
if department:
student["Department"] = department
if marks_input:
try:
marks = float(marks_input)
if marks < 0 or marks > 100:
print("Marks must be between 0 and 100!")
return
student["Marks"] = marks
except ValueError:
print("Invalid marks!")
return
save_students(students)
print("Student record updated successfully!")
return
print("Student not found!")
# Main menu
def main():
while True:
print("\n===== STUDENT DATA MANAGER =====")
print("1. Add Student")
print("2. Display Students")
print("3. Search Student")
print("4. Update Student")
print("5. Exit")
choice = input("Enter your choice: ")
if choice == "1":
add_student()
elif choice == "2":
display_students()
elif choice == "3":
search_student()
elif choice == "4":
update_student()
elif choice == "5":
print("Thank you!")
break
else:
print("Invalid choice! Try again.")
