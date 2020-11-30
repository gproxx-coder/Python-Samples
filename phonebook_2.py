phonebook = {}


def add_contact():
    fname = input("Enter first name: ").strip()
    lname = input("Enter last name: ").strip()
    mobile_number = int(input("Enter mobile number: "))
    phonebook[mobile_number] = {0: fname, 1: lname}
    # print(phonebook)


def view_contacts():
    if len(phonebook) < 1:
        print("The phonebook is empty. Please add some.")
    else:
        for contact in phonebook:
            print(phonebook[contact][0] + " " + phonebook[contact][1], "-", contact)


def search_contact():
    if len(phonebook) < 1:
        print("The phonebook is empty. Please add some.")
    else:
        to_find = input("Enter number or name: ")
        if to_find.isalpha():
            for number, name in phonebook.items():
                if to_find in name[0] or to_find in name[1]:
                    print(f"{name[0]} {name[1]} - {number}")
        elif int(to_find) in phonebook:
            print(f"{phonebook[int(to_find)][0]} {phonebook[int(to_find)][1]} - {to_find}")
        else:
            print("Sorry contact not found !!")


def remove_contact():
    if len(phonebook) < 1:
        print("The phonebook is empty. Please add some.")
    else:
        view_contacts()
        to_delete = input("Which contact you want to delete ?\nEnter Number: ")
        err = phonebook.pop(int(to_delete), 0)
        if err == 0:
            print("Please try again. Incorrect credentials. ")
        else:
            print("Contact deleted successfully. ")


operations = {1: add_contact,
              2: view_contacts,
              3: search_contact,
              4: remove_contact, }
choice = 0
while True:
    try:
        print("\n~~Operations~~")
        choice = int(input("1. Add Contact   2. View All Contacts   3. Find Contact  4. Remove Contact  5. Exit \n"))
        if 0 < choice < 5:
            func = operations[choice]
            func()
        elif choice == 5:
            break
        else:
            print("Please enter only digit in 1-5 range !!")
    except ValueError:
        print("Please enter only digit in 1-5 range !!")
