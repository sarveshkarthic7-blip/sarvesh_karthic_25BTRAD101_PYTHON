# Library Management System Using OOP
# Parent class
class LibraryItem:
def __init__(self, book_id, title):
self.book_id = book_id
self.title = title
# Child class
class Book(LibraryItem):
def __init__(self, book_id, title, author):
super().__init__(book_id, title)
self.author = author
self.__available = True
self.issued_to = None
# Issue book
def issue_book(self, student_name):
if self.__available:
self.__available = False
self.issued_to = student_name
print("Book issued successfully!")
else:
print("Book is already issued!")
# Return book
def return_book(self):
if not self.__available:
self.__available = True
self.issued_to = None
print("Book returned successfully!")
else:
print("Book was not issued!")
# Check availability
def display_book(self):
print("\nBook ID:", self.book_id)
print("Title:", self.title)
print("Author:", self.author)
if self.__available:
print("Status: Available")
else:
print("Status: Issued")
print("Issued To:", self.issued_to)
# Library management class
class Library:
def __init__(self):
self.books = [
Book(101, "Python Programming", "Guido"),
Book(102, "Data Structures", "Mark Allen"),
Book(103, "Computer Networks", "Andrew"),
Book(104, "Operating Systems", "Galvin")
]
# Search book using ID
def find_book(self, book_id):
for book in self.books:
if book.book_id == book_id:
return book
return None
# Display all books
def display_books(self):
print("\n===== LIBRARY BOOKS =====")
for book in self.books:
book.display_book()
# Issue a book
def issue(self):
try:
book_id = int(input("Enter Book ID: "))
book = self.find_book(book_id)
if book:
student = input("Enter student name: ").strip()
if student:
book.issue_book(student)
else:
print("Student name cannot be empty!")
else:
print("Book not found!")
except ValueError:
print("Please enter a valid Book ID!")
# Return a book
def return_book(self):
try:
book_id = int(input("Enter Book ID: "))
book = self.find_book(book_id)
if book:
book.return_book()
else:
print("Book not found!")
except ValueError:
print("Please enter a valid Book ID!")
# Main program
def main():
library = Library()
while True:
print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
print("1. Display All Books")
print("2. Issue Book")
print("3. Return Book")
print("4. Exit")
try:
choice = int(input("Enter your choice: "))
if choice == 1:
library.display_books()
elif choice == 2:
library.issue()
elif choice == 3:
library.return_book()
elif choice == 4:
break
print("Thank you for using the library system!")
else:
print("Invalid choice! Try again.")
except ValueError:
print("Please enter a valid menu choice!")
main()
