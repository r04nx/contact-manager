import os

print("--- Welcome to Contact Manager ---")

if os.path.exists('contact.db'):
    with open('contact.db', 'r') as file:
        contact = file.read()
        num = contact.count("\n")
        print("Number of Contacts: " + str(num))
        file.close()


def updateContact(nam):
    with open('contact.db', 'r') as file:
        contacts = file.readlines()
        dict = {}
        result = ""
        flag = 0
        for item in contacts:
            key, value = item.strip().split(":")
            dict[key] = value  # Created Dict of Contacts
        for name in dict.keys():
            if nam in name:
                flag = 1
        file.close()

    if (flag == 1):
        for name, num in dict.items():
            if nam == name:
                print("Name: " + name + "\nContact: " + num)
                print("What do you want to edit? (Name[N] or Contact Number[C])")
                ans = input(">").capitalize()
                if (ans == "N"):
                    name_ = input("Name to be updated: ")
                    tmp = dict[nam]
                    dict.pop(nam)
                    dict[name_] = tmp
                if ans == "C":
                    contact_ = input("Number to be updated: ")
                    dict[nam] = contact_
                for key, value in dict.items():
                    result += f"{key}:{value}\n"
                with open('contact.db', 'w') as file:
                    file.write(result)
                    file.close()
                return "Updated Successfully!"
    else:
        return "Contact not found!"


def viewAll():
    with open('contact.db', 'r') as file:
        contacts = file.readlines()
        print("Contact list: ")
        for contact in contacts:
            print("_______________________________".replace("_", "-"))
            row = contact.strip().split(":")
            print("Name: {0} \nContact: {1}".format(row[0], row[1]), end="\n")
        print("_______________________________".replace("_", "-"))
    print("\n\n")


def searchContact(name):
    with open('contact.db', 'r') as file:
        contacts = file.readlines()
        counter = 0
        rcontact = ""
        # print(contacts)
        for contact in contacts:
            if name.upper() in contact.upper():
                counter += 1
                rcontact += "_______________________________\n".replace("_", "-")
                rcontact += "Name: " + contact.replace(":", "\nContact: ")
        file.close()
        if rcontact == "":
            return "Contact not Found!"
        else:
            return "----- " + str(counter) + " Contact found! -----\n" + rcontact + "_______________________________".replace("_", "-")


def addContact(name, number):
    if not os.path.exists('contact.db'):
        with open("contact.db", 'w+') as file:
            file.write(name + ":" + number + "\n")
    else:
        flag = 0
        with open('contact.db', 'r') as file:
            contacts = file.readlines()
            for contact in contacts:
                if (name == contact.split(":")[0]):
                    print("Name already exists!")
                    flag = 1
        if (flag == 0):
            with open("contact.db", 'a') as file:
                file.write(name + ":" + number + "\n")

                file.close()
            print("Contact Inserted Successfully!")



def delContact(name):
    with open('contact.db', 'r') as file:
        contacts = file.readlines()
        counter = 0
        cdel=0
        dict = set({})
        to_del = []
        rcontact = ""
        for contact in contacts:
           dict.add(contact)

        for contact in contacts:
            if name.upper() in contact.upper():
                to_del.append(contact)
                cdel += 1
                rcontact += "_______________________________\n".replace("_", "-")
                rcontact += "[" + str(cdel) + "] Name: " + contact.replace(":", "\nContact: ")
                file.close()

    with open('contact.db', 'w') as file:
        if len(to_del) > 1:
                print("----- " + str(cdel) + " Contact found! -----\n" + rcontact + "_______________________________".replace("_", "-"))
                print("Select the contact to delete & enter(Q) to quit!): ")
                ansn = int(input(">"))
                ansn -=1

                if str(ansn).upper() == 'Q':
                    return "Aborted!"
                else:
                    print("Are you sure, to delete the contact? (Y/N)")
                    ans = input(">")
                    if ans.upper() == "Y" or ans.upper() == "yes" or ans.upper() == "YES" or ans.upper() == "Yes":
                        dict.remove(to_del[ansn])
                        for contact in dict:
                            file.write(contact)
                        file.close()
                        return "Contact deleted!\n"
                    else:
                        return "Aborted!\n"

        if len(to_del) == 0:
            print("----- " + str(cdel) + " Contact found! -----\n" + rcontact + "_______________________________".replace("_", "-"))
            return "Contact not found!"

        else:
            print("----- " + str(cdel) + " Contact found! -----\n" + rcontact + "_______________________________".replace("_", "-"))
            print("Are you sure, to delete the contact? (Y/N)")
            ans = input(">")
            ansn = 0
            if ans.upper() == "Y" or ans.upper() == "yes" or ans.upper() == "YES" or ans.upper() == "Yes":
                dict.remove(to_del[ansn])
                for contact in dict:
                    file.write(contact)
                file.close()

                return "Contact deleted!\n"
            else:
                return "Aborted!\n"


while (True):
    print("Choose from the given options:\n"
          "(A) Add Contact\n"
          "(S) Search Contact\n"
          "(U) Update Contact\n"
          "(D) Delete Contact\n"
          "(V) View all Contacts\n"
          "(Q) Quit")
    menu = input(">")

    if menu == "A" or menu == "a":
        name = str(input("Name: "))
        number = str(input("Contact No.: "))
        addContact(name, number)

    if menu == "S" or menu == "s":
        name = input("Enter the name to search in contact: ")
        result = searchContact(name)
        print(result)

    if menu == "U" or menu == "u":
        name = input("Enter the contact name to edit: ")
        print(updateContact(name))

    if menu == "V" or menu == "v":
        viewAll()

    if menu == "D" or menu == "d":
        name = input("Enter the contact name to delete: ")
        print(delContact(name))

    if menu == "Q" or menu == "q":
        print("Bye!")
        quit()
