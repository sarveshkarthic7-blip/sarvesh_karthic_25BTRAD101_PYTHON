attendance = {}
def add_student():
name = input("Enter student name: ")
if name not in attendance:
attendance[name] = []
print("Student added successfully!")
else:
print("Student already exists!")
def mark_attendance():
name = input("Enter student name: ")
if name in attendance:
status = input("Enter P for Present or A for Absent: ").upper()
if status == "P" or status == "A":
attendance[name].append(status)
print("Attendance marked successfully!")
else:
print("Invalid status!")
else:
print("Student not found!")
def display_attendance():
print("\n--- Attendance Records ---")
for name, records in attendance.items():
total = len(records)
present = records.count("P")
absent = records.count("A")
if total > 0:
percentage = (present / total) * 100
else:
percentage = 0
print("\nName:", name)
print("Present:", present)
print("Absent:", absent)
print("Attendance:", round(percentage, 2), "%")
def check_shortage():
print("\n--- Attendance Shortage ---")
for name, records in attendance.items():
total = len(records)
present = records.count("P")
percentage = (present / total * 100) if total > 0 else 0
if percentage < 75:
print(name,
"-"
, round(percentage, 2), "%")
def main():
while True:
print("\n===== ATTENDANCE TRACKER =====")
print("1. Add Student")
print("2. Mark Attendance")
print("3. Display Attendance")
print("4. Check Attendance Shortage")
print("5. Exit")
choice = input("Enter your choice: ")
if choice == "1":
add_student()
elif choice == "2":
mark_attendance()
elif choice == "3":
display_attendance()
elif choice == "4":
check_shortage()
elif choice == "5":
print("Thank you!")
break
else:
print("Invalid choice!")
main()
