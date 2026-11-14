students = {}
n = int(input("Enter number of students: "))
for i in range(n):
name = input("Enter student name: ")
marks = int(input("Enter student marks: "))
students[name] = marks
print("\n--- Student Grading Results ---")
for name, marks in students.items():
if marks >= 90:
grade = "A"
elif marks >= 80:
grade = "B"
elif marks >= 70:
grade = "C"
elif marks >= 60:
grade = "D"
else:
grade = "F"
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)
print("--------------------")
