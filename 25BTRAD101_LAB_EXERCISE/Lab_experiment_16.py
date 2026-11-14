import random
# Function to roll dice
def roll_dice(number_of_dice):
results = []
for i in range(number_of_dice):
result = random.randint(1, 6)
results.append(result)
return results
# Function to display frequency
def display_frequency(all_results):
frequency = {
1: 0,
2: 0,
3: 0,
4: 0,
5: 0,
6: 0
}
for result in all_results:
frequency[result] += 1
print("\n===== DICE FREQUENCY =====")
for face, count in frequency.items():
print("Face", face, ":", count, "times")
# Main program
def main():
all_results = []
print("===== DICE ROLLING SIMULATOR =====")
while True:
print("\n1. Roll Dice")
print("2. Display Frequency")
print("3. Exit")
try:
choice = int(input("Enter your choice: "))
if choice == 1:
number = int(input("Enter number of dice: "))
if number <= 0:
continue
print("Please enter a positive number!")
results = roll_dice(number)
print("\nDice Results:", results)
all_results.extend(results)
elif choice == 2:
if not all_results:
print("No rolls have been performed yet!")
else:
display_frequency(all_results)
elif choice == 3:
print("\nThank you for using Dice Simulator!")
break
else:
print("Invalid choice! Try again.")
except ValueError:
print("Please enter valid numeric input!")
main()
