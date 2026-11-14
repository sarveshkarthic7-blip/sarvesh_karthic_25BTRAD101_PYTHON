# Bank Account System Using OOP
class BankAccount:
# Constructor
def __init__(self, account_holder, account_number, balance=0):
self.account_holder = account_holder
self.account_number = account_number
self.__balance = balance
# Deposit money
def deposit(self, amount):
if amount <= 0:
print("Invalid amount! Deposit must be positive.")
else:
self.__balance += amount
print("Rs.", amount, "deposited successfully!")
# Withdraw money
def withdraw(self, amount):
if amount <= 0:
print("Invalid amount! Withdrawal must be positive.")
elif amount > self.__balance:
print("Insufficient balance!")
else:
self.__balance -= amount
print("Rs.", amount, "withdrawn successfully!")
# Check account balance
def balance_enquiry(self):
print("\nAccount Holder:", self.account_holder)
print("Account Number:", self.account_number)
print("Available Balance: Rs.", self.__balance)
# Main program
def main():
print("===== BANK ACCOUNT SYSTEM =====")
name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
account = BankAccount(name, account_number)
while True:
print("\n===== BANK MENU =====")
print("1. Deposit Money")
print("2. Withdraw Money")
print("3. Balance Enquiry")
print("4. Exit")
try:
choice = int(input("Enter your choice: "))
if choice == 1:
amount = float(input("Enter deposit amount: "))
account.deposit(amount)
elif choice == 2:
amount = float(input("Enter withdrawal amount: "))
account.withdraw(amount)
elif choice == 3:
account.balance_enquiry()
elif choice == 4:
print("Thank you for using our banking system!")
break
else:
print("Invalid choice! Please try again.")
except ValueError:
print("Invalid input! Please enter a valid number.")
main()
