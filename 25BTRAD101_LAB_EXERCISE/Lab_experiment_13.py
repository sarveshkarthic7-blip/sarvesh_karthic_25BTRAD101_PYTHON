import csv
import os
FILENAME = "employees.csv"
# Function to calculate employee salary
def calculate_salary(employee):
basic = float(employee["Basic_Salary"])
hra = basic * 0.20
da = basic * 0.10
gross = basic + hra + da
pf = basic * 0.12
tax = gross * 0.05
total_deductions = pf + tax
net_salary = gross - total_deductions
return {
"Employee_ID": employee["Employee_ID"],
"Name": employee["Name"],
"Basic": basic,
"HRA": hra,
"DA": da,
"Gross": gross,
"PF": pf,
"Tax": tax,
"Deductions": total_deductions,
"Net": net_salary
}
# Function to read employee records
def read_employees():
employees = []
try:
with open(FILENAME, "r", newline=
"") as file:
reader = csv.DictReader(file)
required_fields = {
"Employee_ID", "Name", "Basic_Salary"
}
if not required_fields.issubset(reader.fieldnames or []):
print("Invalid CSV file format!")
return None
for row in reader:
try:
if not row["Employee_ID"].strip():
raise ValueError("Missing Employee ID")
if not row["Name"].strip():
raise ValueError("Missing employee name")
basic = float(row["Basic_Salary"])
if basic < 0:
raise ValueError("Negative salary")
employees.append(row)
except (ValueError, AttributeError):
print("Invalid employee record skipped:", row)
return employees
except FileNotFoundError:
print("Error: Employee CSV file not found!")
return None
# Function to generate payroll report
def generate_report():
employees = read_employees()
if employees is None:
return
if not employees:
return
print("No valid employee records found!")
total_gross = 0
total_deductions = 0
total_net = 0
print("\n========== PAYROLL REPORT ==========")
for employee in employees:
salary = calculate_salary(employee)
print("\nEmployee ID:", salary["Employee_ID"])
print("Name:", salary["Name"])
print("Basic Salary: Rs.", round(salary["Basic"], 2))
print("HRA: Rs.", round(salary["HRA"], 2))
print("DA: Rs.", round(salary["DA"], 2))
print("Gross Salary: Rs.", round(salary["Gross"], 2))
print("PF: Rs.", round(salary["PF"], 2))
print("Tax: Rs.", round(salary["Tax"], 2))
print("Total Deductions: Rs.", round(salary["Deductions"], 2))
print("Net Salary: Rs.", round(salary["Net"], 2))
total_gross += salary["Gross"]
total_deductions += salary["Deductions"]
total_net += salary["Net"]
# Display overall summary
print("\n========== SALARY SUMMARY ==========")
print("Total Employees:", len(employees))
print("Total Gross Salary: Rs.", round(total_gross, 2))
print("Total Deductions: Rs.", round(total_deductions, 2))
print("Total Net Salary: Rs.", round(total_net, 2))
print("\nPayroll calculation completed!")
# Main program
if __name__ == "__main__":
if os.path.exists(FILENAME):
generate_report()
else:
print("Employee file does not exist!")
