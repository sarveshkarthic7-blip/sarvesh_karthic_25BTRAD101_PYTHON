def read_log_file(filename):
# Initialize counters
count = {
"ERROR": 0,
"WARNING": 0,
"INFO": 0
}
try:
# Open the log file
with open(filename, "r") as file:
lines = file.readlines()
# Check whether file is empty
if not lines:
print("The log file is empty!")
return
# Read each line
for line in lines:
if "ERROR" in line:
count["ERROR"] += 1
elif "WARNING" in line:
count["WARNING"] += 1
elif "INFO" in line:
count["INFO"] += 1
# Display results
print("\n===== LOG FILE SUMMARY =====")
print("Total Log Entries:", len(lines))
print("ERROR Count:", count["ERROR"])
print("WARNING Count:", count["WARNING"])
print("INFO Count:", count["INFO"])
print("\nLog Analysis Completed!")
except FileNotFoundError:
print("Error: Log file not found!")
except PermissionError:
print("Error: Permission denied!")
# Main program
filename = "application.log"
read_log_file(filename)
