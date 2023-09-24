import os

def display_menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Exit")

def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"{name} has been added to your contacts!")

def view_contacts(contacts):
    if not contacts:
        print("Your contact book is empty.")
    else:
        print("\nContacts:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print("-" * 20)

def search_contacts(contacts):
    search_name = input("Enter the name to search for: ")
    contact = contacts.get(search_name)
    if contact:
        print("\nContact Details:")
        print(f"Name: {search_name}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}")
    else:
        print(f"No contact found with the name {search_name}.")

def save_contacts(contacts, filename):
    with open(filename, 'w') as file:
        for name, info in contacts.items():
            file.write(f"{name},{info['Phone']},{info['Email']}\n")

def load_contacts(filename):
    contacts = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, phone, email = line.strip().split(',')
                contacts[name] = {"Phone": phone, "Email": email}
    return contacts

def main():
    contacts_file = "contacts.txt"
    contacts = load_contacts(contacts_file)

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            save_contacts(contacts, contacts_file)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
