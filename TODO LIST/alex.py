tasks = []

while True:
    print("\n=== Task list ===")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark as done")
    print("4. Delete task")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        text = input("New task: ")
        tasks.append({"text": text, "done": False})
        print("Task added.")
    elif choice == "2":
        if not tasks:
            print("You have no tasks.")
        else:
            for i, item in enumerate(tasks, start=1):
                status = "[x]" if item["done"] else "[ ]"
                print(f"{i}. {status} {item['text']}")
    elif choice == "3":
        index = int(input("Number of the task to mark done: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            print("Marked as done.")
        else:
            print("Invalid number.")
    elif choice == "4":
        index = int(input("Number of the task to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Stearsa: {removed['text']}")
        else:
            print("Invalid number.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")