﻿# Contact Manager Python Project

The **Contact Manager** is a simple Python program designed to help you manage and manipulate contact information. It provides a command-line interface to perform various tasks related to contacts, such as adding, searching, updating, and deleting contacts.

## Features

- **View All Contacts**: View the list of all saved contacts with their names and contact numbers.

- **Add Contact**: Add new contacts to the contact list by providing a name and contact number. The information is stored in the 'contact.db' file.

- **Search Contact**: Search for a contact by name and retrieve information about matching contacts. The search is case-insensitive.

- **Update Contact**: Modify the details of a contact, including changing the contact name or contact number.

- **Delete Contact**: Delete one or multiple contacts from the contact list. You can choose which contacts to delete based on your selection.

## Usage

1. Run the script using a Python interpreter:
   ```shell
   python app.py
   ```

2. Choose from the available options:
   - **A**: Add Contact
   - **S**: Search Contact
   - **U**: Update Contact
   - **D**: Delete Contact
   - **V**: View All Contacts
   - **Q**: Quit

3. Follow the prompts to perform the desired action.

Implementation Details
Contacts are stored as a dictionary in memory, which enhances performance by reducing frequent file reads and writes.

The load_contacts function reads contacts from the 'contact.db' file into a dictionary.

The save_contacts function writes the dictionary back to the file after modifications.

The update_contact function allows you to edit existing contact details, such as the name or contact number.

The search_contact function searches for contacts containing a specified name and displays matching results.

The add_contact function adds new contacts to the dictionary and updates the 'contact.db' file.

The del_contact function removes contacts from the dictionary and updates the 'contact.db' file.

## Disclaimer

This project is for educational and practice purposes. It demonstrates basic file handling, command-line interface, and data manipulation concepts using Python.

---
