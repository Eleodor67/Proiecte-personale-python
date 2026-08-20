#tasks: 1. taskurile sa inceapa de la 1 nu de la 0, 2. erorile cu str si float 3. eroare task gol(enter)
decision_number=int(1)
tasks=[]
print("""=== Task list ===
        1. Add task
        2. Show tasks
        3. Mark as done
        4. Delete task
        5. Exit""")
while True:
    
    if (decision_number==5):
        print("You closed the program")
        exit()
    else:
        decision_number= int(input("Choose an option: "))
        if(decision_number >= 1 and decision_number<=5):
            pass
        else:
            print("Choose a number between 1 and 5")
    if(decision_number==1):
        tasks.append("[ ]"+ input("New task: "))
        print("Task added")
    if(decision_number==2):
        if(len(tasks)<1):
            print("There are no tasks added")
        else:
            print("All your tasks: ")
            for i in range(len(tasks)):
                print(f"{i}. "+ tasks[i])
    if(decision_number==3):
        if(len(tasks)>0):
            for i in range(len(tasks)):
                            print(f"{i}. "+ tasks[i])
            mark_as_done=int(input("Choose what tasks you want to mark as done: "))
            if(mark_as_done<=len(tasks)):
                tasks[mark_as_done]=tasks[mark_as_done].replace("[ ]","[x]")
            else:
                print("Please choose a valid number")
                continue
        else:
             print("There are not any tasks yet")

    if(decision_number==4):
        if(len(tasks)>0):
            for i in range(len(tasks)):
                print(f"{i}. "+ tasks[i])

            mark_for_delete=int(input("Choose what tasks you want to delete: "))
            if(mark_for_delete<=len(tasks)):
                tasks.pop(mark_for_delete)
            else:
                print("Please choose a valid number")
                continue
        else:
            print("There are no tasks added")
    
    