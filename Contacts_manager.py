# Contact Management System
# Week 3 Project - Functions & Dictionaries


import json
import csv
from datetime import datetime

# ---------------- DATA ----------------
contacts = {}

DATA_FILE = "contacts_data.json"

# ---------------- VALIDATION ----------------
def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def validate_email(email):
    return email == "" or ("@" in email and "." in email)

# ---------------- FILE OPERATIONS ----------------
def load_contacts():
    global contacts
    try:
        with open(DATA_FILE, "r") as f:
            contacts = json.load(f)
        print("\nContacts loaded successfully!")
    except FileNotFoundError:
        contacts = {}
        print("\nNo existing contacts file found. Starting fresh.")

def save_contacts():
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)
    print(f"\nContacts saved to {DATA_FILE}")

def backup_contacts():
    filename = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(contacts, f, indent=4)
    print(f"\nBackup created: {filename}")

# ---------------- DISPLAY ----------------
def display_contact(name, data, index=None):
    if index is not None:
        print(f"{index}. {name}")
    else:
        print(f"{name}")

    print(f"   Phone: {data['phone']}")
    print(f"   Email: {data['email']}")
    print(f"   Address: {data['address']}")
    print(f"   Group: {data['group']}")
    print("-" * 40)

# ---------------- CRUD ----------------
def add_contact():
    print("\nADD NEW CONTACT")

    name = input("Enter contact name: ").strip()

    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter phone number: ").strip()
    while not validate_phone(phone):
        phone = input("Enter valid 10-digit phone: ").strip()

    email = input("Enter email (optional, press Enter to skip): ").strip()
    while email != "" and not validate_email(email):
        email = input("Enter valid email: ").strip()

    address = input("Enter address: ").strip()
    group = input("Enter group: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address,
        "group": group
    }

    print(f"Contact '{name}' added successfully!")
    save_contacts()

def search_contact():
    key = input("Enter name to search: ").lower()

    found = False
    count = 1

    print("\nSearch Results:")

    for name, data in contacts.items():
        if key in name.lower():
            display_contact(name, data, count)
            count += 1
            found = True

    if not found:
        print("No contact found.")

def update_contact():
    name = input("Enter name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    print("Leave blank to keep current value.")

    phone = input("New phone: ").strip()
    if phone:
        while not validate_phone(phone):
            phone = input("Invalid phone. Enter again: ")
        contacts[name]["phone"] = phone

    email = input("New email: ").strip()
    if email:
        while not validate_email(email):
            email = input("Invalid email. Enter again: ")
        contacts[name]["email"] = email

    address = input("New address: ").strip()
    if address:
        contacts[name]["address"] = address

    group = input("New group: ").strip()
    if group:
        contacts[name]["group"] = group

    print("Contact updated successfully!")
    save_contacts()

def delete_contact():
    name = input("Enter name to delete: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    confirm = input("Are you sure? (yes/no): ").lower()

    if confirm == "yes":
        del contacts[name]
        print("Contact deleted successfully!")
        save_contacts()
    else:
        print("Deletion cancelled.")

def view_all():
    if not contacts:
        print("No contacts available.")
        return

    print(f"\nALL CONTACTS ({len(contacts)} total)")

    i = 1
    for name, data in contacts.items():
        display_contact(name, data, i)
        i += 1

# ---------------- EXPORT ----------------
def export_csv():
    with open("contacts.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email", "Address", "Group"])

        for name, data in contacts.items():
            writer.writerow([
                name,
                data["phone"],
                data["email"],
                data["address"],
                data["group"]
            ])

    print("Contacts exported to contacts.csv")

# ---------------- STATISTICS ----------------
def show_stats():
    print("\nCONTACT STATISTICS")
    print("Total Contacts:", len(contacts))

    groups = {}

    for data in contacts.values():
        g = data.get("group", "Other")
        groups[g] = groups.get(g, 0) + 1

    print("\nContacts by Group:")
    for k, v in groups.items():
        print(k + ":", v)

# ---------------- MENU ----------------
def menu():
    print("\n==============================")
    print("CONTACT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add New Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Export to CSV")
    print("7. View Statistics")
    print("8. Exit")
    print("==============================")

def get_choice():
    while True:
        c = input("Enter your choice (1-8): ").strip()
        if c in ["1","2","3","4","5","6","7","8"]:
            return c
        print("Invalid choice")

# ---------------- MAIN ----------------
print("\nCONTACT MANAGEMENT SYSTEM")

load_contacts()

while True:
    menu()
    choice = get_choice()

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        view_all()
    elif choice == "6":
        export_csv()
    elif choice == "7":
        show_stats()
    elif choice == "8":
        save_contacts()
        print("\n==============================")
        print("Thank you for using Contact Management System")
        print("==============================")
        break
