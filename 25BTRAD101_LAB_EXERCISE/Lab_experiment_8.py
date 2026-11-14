contacts = []
while True:
print("\n--- Contact Book ---")
print("1. Add Contact")
print("2. Search Contact")
print("3. Update Contact")
print("4. Delete Contact")
print("5. Display Contacts")
print("6. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
name = input("Enter contact name: ")
phone = input("Enter phone number: ")
contact = {"name": name, "phone": phone}
contacts.append(contact)
print("Contact added successfully!")
elif choice == 2:
name = input("Enter name to search: ")
found = False
for contact in contacts:
if contact["name"].lower() == name.lower():
print("Name:", contact["name"])
print("Phone:", contact["phone"])
found = True
break
if found == False:
print("Contact not found!")
elif choice == 3:
name = input("Enter name to update: ")
found = False
for contact in contacts:
if contact["name"].lower() == name.lower():
contact["phone"] = input("Enter new phone number: ")
print("Contact updated successfully!")
found = True
break
if found == False:
print("Contact not found!")
elif choice == 4:
name = input("Enter name to delete: ")
found = False
for contact in contacts:
if contact["name"].lower() == name.lower():
contacts.remove(contact)
print("Contact deleted successfully!")
found = True
break
if found == False:
print("Contact not found!")
elif choice == 5:
if len(contacts) == 0:
print("Contact book is empty!")
else:
for contact in contacts:
print("Name:", contact["name"])
print("Phone:", contact["phone"])
print("--------------------")
elif choice == 6:
print("Exiting Contact Book.")
break
else:
print("Invalid choice!")
