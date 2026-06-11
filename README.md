# Contact Management System

## Project Description

A comprehensive Contact Management System built with Python using dictionaries, functions, file handling, and input validation. This application allows users to manage contacts through a user-friendly menu interface with full CRUD (Create, Read, Update, Delete) operations, search functionality, statistics, and data persistence using JSON files.

---

## What I Learned

### 1. Functions

* Creating reusable and organized code blocks
* Passing arguments and returning values
* Separating functionality into logical components

### 2. Dictionaries

* Storing data using key-value pairs
* Using nested dictionaries for structured contact information
* Searching and updating dictionary data efficiently

### 3. String Methods

* Case-insensitive searching using `lower()`
* Input cleaning with `strip()`
* Formatting output for better readability

### 4. File Operations

* Reading and writing JSON files
* Exporting data to CSV format
* Creating backup files

### 5. Input Validation

* Validating phone numbers
* Validating email addresses
* Handling invalid user input

### 6. Error Handling

* Managing file-related exceptions
* Preventing application crashes from invalid data
* Providing user-friendly error messages

---

## Features

*  Add new contacts with validation
*  Search contacts by name (partial matching supported)
*  Update existing contact information
*  Delete contacts with confirmation
*  View all contacts in formatted display
*  Save contacts to JSON file automatically
*  Load contacts from file on startup
*  Export contacts to CSV format
*  Contact statistics and analytics
*  Phone number and email validation
*  User-friendly menu interface
*  Error handling for all operations

---

## How to Run

### Navigate to Project Folder

```bash
cd week3-contact-manager
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run the Program

```bash
python contacts_manager.py
```

### Run Tests

```bash
python test_contacts.py
```

---

## Data Structure

```python
contacts = {
    "John Doe": {
        "phone": "1234567890",
        "email": "john@example.com",
        "address": "123 Main St",
        "group": "Friends"
    },
    "Jane Smith": {
        "phone": "0987654321",
        "email": "jane@example.com",
        "address": "456 Oak Ave",
        "group": "Work"
    }
}
```

---

## Sample Menu

```text
===========================================
      CONTACT MANAGEMENT SYSTEM
===========================================
1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Exit

Enter your choice (1-8):
```

---

## Sample Output

```text
Search Results for 'john':
------------------------------------------
1. John Doe
   Phone: 1234567890
   Email: john@example.com
   Address: 123 Main St
   Group: Friends

2. Johnny Appleseed
   Phone: 5551234567
   Email: johnny@apple.com
   Address: 789 Orchard Rd
   Group: Family
------------------------------------------
Found 2 contacts matching 'john'

Statistics:
- Total Contacts: 15
- Friends: 5 contacts
- Work: 7 contacts
- Family: 3 contacts
```

---

## Technical Requirements Completed

### Functions

* add_contact()
* search_contact()
* update_contact()
* delete_contact()
* display_all()
* save_contacts()
* load_contacts()
* export_csv()
* show_stats()

### Dictionaries

* Nested dictionary structure for storing contacts
* Dynamic addition, modification, and deletion of entries

### File Handling

* JSON save/load functionality
* CSV export support
* Backup file creation

### Validation

* Phone number validation
* Email validation
* Menu choice validation

### Searching

* Partial name matching
* Case-insensitive search

---

## Challenges & Solutions

### Challenge: Handling Duplicate Contact Names

**Solution:** Added duplicate checking before creating a new contact.

### Challenge: Phone Number Validation

**Solution:** Created a validation function that ensures phone numbers contain exactly 10 digits.

### Challenge: Efficient Search with Partial Matching

**Solution:** Used `lower()` and substring matching for case-insensitive searches.

### Challenge: Data Persistence

**Solution:** Implemented JSON file storage with automatic loading and saving.

### Challenge: User Input Errors

**Solution:** Added validation loops and clear error messages for all user inputs.

---

## Project Structure

```text
week3-contact-manager/
│
├── contacts_manager.py
├── test_contacts.py
├── contacts_data.json
├── contacts.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Conclusion

This project demonstrates the practical use of Python functions, dictionaries, file handling, validation, and menu-driven applications. It provides a solid foundation for building larger data management systems and reinforces core programming concepts through a real-world application.
