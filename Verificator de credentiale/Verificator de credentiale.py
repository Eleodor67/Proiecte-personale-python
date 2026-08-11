username="admin"
password="admin_12345!"
attempts_failed=3
attempts=1
failed_attempt=0
print("=== Login system ===")
while attempts<4:
    print(f"Attempt {attempts} of 3")
    entered_username=input("Username: ")
    entered_password=input("Password: ")
    if(entered_username=="" or entered_password==""):
        print("Fields cannot be empty.")
        continue
    is_username_corect=entered_username==username
    is_password_corect=entered_password==password
    attempts+=1
    attempts_failed-=1
    if is_username_corect and is_password_corect:
        print("Login successful! Welcome, admin.")
        failed_attempt=1
        break
    elif not is_username_corect and not is_password_corect:
        print(f"Wrong username and password. You have {attempts_failed} attempts left.")   
    elif not is_username_corect:
        print(f"Wrong username. You have {attempts_failed} attempts left.")
    elif not is_password_corect:
        print(f"Wrong password. You have {attempts_failed} attempts left.")

if failed_attempt==0:
    print("Account locked after 3 failed attempts.")