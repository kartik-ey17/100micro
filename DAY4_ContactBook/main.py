from dataclasses import dataclass , asdict

def search_contacts(search_term , contacts):
    query = search_term.lower().strip()

    results = [contact for contact in contacts if query in contact["name"].lower()]
    return results

def view(contacts):
    for contact in contacts:
        print(contact["sr"] , ". Name : " ,contact["name"] , "\nPhone Number : " , contact["PhoneNumber"] , "\nE-mail : " , contact["email"] , "\nRemark : " , contact["remark"] , "\n-------------------------------------")

@dataclass
class Person:
    sr: int = 0
    name: str = "Unknown"
    PhoneNumber: str = "0000000000"
    email: str = "_"
    remark: str = "None"

contacts = []

sr = 0

cont = True
while cont:
    print("+=+=+= Contact Book =+=+=+")
    choice = int(input("1.Add Contact\n2.View Contacts\n3.Search Contacts\n4.Update Contacts\n5.Delete Contacts\n6.Exit\nChoice : "))
    if choice == 1:
        name = input("Enter the name of the contact : ")
        phone = input("Enter the phone number : ")
        email = input("Enter the email of the contact : ")
        remark = input("Enter any remark about the person : ")
        sr += 1
        p = Person(sr , name , phone , email , remark)

        contacts.append(asdict(p))
        
    elif choice == 2:
        view(contacts)

    elif choice == 3:
        print('----- Search Contacts -----\n')
        search = input("Enter search query : ")
        matches = search_contacts(search , contacts)
        if matches:
            print(f"Found {len(matches)} matching contacts.")
            for contact in matches:
                print(f" - {contact['name']} , - {contact['PhoneNumber']}")
        else:
           print("No contacts found.")

    elif choice == 4:
        print("----- Update a contact -----")
        view(contacts)
        update = int(input("Enter the serial number of the contact you want to change : "))
        for contact in contacts:
            if contact["sr"] == update:
                update_name = input("Enter updated Name : ")
                update_pNo = input("Enter updated Phone Number : ")
                update_email = input("Enter updated email address : ")
                update_remark = input("Enter updated remark : ")
                contact["name"] = update_name
                contact["PhoneNumber"] = update_pNo
                contact["email"] = update_email
                contact["remark"] = update_remark
                print("Updated Contact - \n" , contact)

    elif choice == 5:
        view(contacts)
        delete = int(input("Enter the serial number of the contact you want to delete : "))
        if delete:
            for contact in contacts:
                if contact["sr"] == delete :
                    contact["name"] = "This contact does not exist anymore"
                    contact["PhoneNumber"] = "This contact does not exist anymore"
                    contact["email"] = "This contact does not exist anymore"
                    contact["remark"] = "This contact does not exist anymore"
                    print("New contact book : \n" , contacts)
        else:
            print("Contact not found")
    elif choice == 6:
        cont = False
        print("Sayonara~")
    else:
        continue