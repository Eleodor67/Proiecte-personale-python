def test_error(test):
    try:
        test=int(test)
    except ValueError:
        return False
    else:
        return True

def add_contact():
    key=input("Choose a name: ")
    value=input("Add a phone number: ")
    phone_book.append({key:value})

def show_contacts():
    if len(phone_book)>0:
        i=1
        for contacts in phone_book: 
            print(f"{i}. {contacts}")
            i=i+1
    else:
        print("There are no contacts yet")

def edit_contacts():
    if(len(phone_book)>0):
        show_contacts()
        while True:
            edit_number=input("Choose what number you want to edit: ")
            if test_error(edit_number) and int(edit_number)<=len(phone_book) and int(edit_number)>0:
                break
            else:
                print("Choose a valid number")
        edit_number=int(edit_number)
        edit_number=edit_number-1
        key=input("Choose a new name: ")
        value=input("Add a new phone number: ")
        phone_book[edit_number]={key:value}
    else:
        print("There are no contacts yet")

def delete_contacts():
    if(len(phone_book)>0):
        show_contacts()
        while True:
            delete_number=input("Choose what number you want to edit: ")
            if test_error(delete_number)  and int(delete_number)<=len(phone_book) and int(delete_number)>0:
                break
            else:
                print("Choose a valid number")
        delete_number=int(delete_number)
        delete_number=delete_number-1
        del phone_book[delete_number]
    else:
        print("There are no contacts yet")

phone_book=[]
contacts={}
while True:
    print("""=== Contacts ===
    1. Add contact
    2. Show contacts
    3. Edit contact
    4. Delete contact
    5. Exit""")
    decision_number=input("Choose an option: ")
    test_error(decision_number)
    if(decision_number=="1"):
        add_contact()
    elif (decision_number=="2"):
        show_contacts()
    elif (decision_number=="3"):
        edit_contacts()
    elif (decision_number=="4"):
        delete_contacts()
    elif (decision_number=="5"):
        print("You closed the program")
        exit()
    else:
        print("Choose a valid number!")
