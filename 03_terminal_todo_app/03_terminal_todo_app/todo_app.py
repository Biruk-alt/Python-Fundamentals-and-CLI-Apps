todolist = ["study python", "read a book", "workout"]
while True:
    print("---YOUR TO-DO LIST---")
    for index, item in enumerate(todolist,start=1):
        print(f"{index}. {item}")
    print("\noptions: ")
    print("1.View Tasks")
    print("2.Add Tasks")
    print("3.Mark a task as done")
    print("4.Delete a task")
    print("5.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        for index, item in enumerate(todolist, start=1):
            print(f"{index}. {item}")
    elif choice == "2":
        add_task = input("What do you need to do? ").strip()
        todolist.append(add_task)
        print("task added.")
    elif choice == "3":
        done = input("Which task number did you finish? ").strip()
        mark_done = int(done) - 1
        todolist[mark_done] = f"todolist[mark_done]:[DONE✅]"
    elif choice == "4":
        delete_task = input("Enter the number of the task you want to delete: ").strip()
        delete_task = int(delete_task) - 1
        del todolist[delete_task]
    elif choice == "5":
        print("GOODBYE!")
        break
    else:
        print("Invalid choice.")

