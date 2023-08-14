import os

def load_contacts():
    contacts = {}
    if os.path.exists('contact.db'):
        with open('contact.db', 'r') as file:
            for line in file:
                name, number = line.strip().split(":")
                contacts[name] = number
    return contacts

def save_contacts(contacts):
    with open('contact.db', 'w') as file:
        for name, number in contacts.items():
            file.write(f"{name}:{number}\n")

def update_contact(contacts, name):
    if name in contacts:
        print("Name:", name)
        print("Contact:", contacts[name])
        print("What do you want to edit? (Name[N] or Contact Number[C])")
        ans = input(">").capitalize()
        if ans == "N":
            new_name = input("New name: ")
            contacts[new_name] = contacts.pop(name)
        elif ans == "C":
            new_number = input("New number: ")
            contacts[name] = new_number
        save_contacts(contacts)
        return "Updated Successfully!"
    else:
        return "Contact not found!"

def view_all(contacts):
    print("Contact list:")
    for name, number in contacts.items():
        print("-" * 30)
        print(f"Name: {name}\nContact: {number}")
    print("-" * 30)

def search_contact(contacts, name):
    matching_contacts = []
    for contact_name, number in contacts.items():
        if name.lower() in contact_name.lower():
            matching_contacts.append((contact_name, number))
    if matching_contacts:
        result = []
        for contact_name, number in matching_contacts:
            result.append(f"Name: {contact_name}\nContact: {number}")
        return f"----- {len(matching_contacts)} Contact found! -----\n" + "\n".join(result)
    else:
        return "Contact not Found!"

def add_contact(contacts, name, number):
    if name not in contacts:
        contacts[name] = number
        save_contacts(contacts)
        return "Contact Inserted Successfully!"
    else:
        return "Name already exists!"

def del_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        return "Contact deleted!"
    else:
        return "Contact not found!"

def main():
    contacts = load_contacts()

    while True:
        print("Choose from the given options:")
        print("(A) Add Contact")
        print("(S) Search Contact")
        print("(U) Update Contact")
        print("(D) Delete Contact")
        print("(V) View all Contacts")
        print("(Q) Quit")
        menu = input(">")

        if menu == "A" or menu == "a":
            name = input("Name: ")
            number = input("Contact No.: ")
            print(add_contact(contacts, name, number))

        elif menu == "S" or menu == "s":
            name = input("Enter the name to search in contacts: ")
            result = search_contact(contacts, name)
            print(result)

        elif menu == "U" or menu == "u":
            name = input("Enter the contact name to edit: ")
            print(update_contact(contacts, name))

        elif menu == "V" or menu == "v":
            view_all(contacts)

        elif menu == "D" or menu == "d":
            name = input("Enter the contact name to delete: ")
            print(del_contact(contacts, name))

        elif menu == "Q" or menu == "q":
            print("Bye!")
            break

if __name__ == "__main__":
    print("--- Welcome to Contact Manager ---")
    main()
