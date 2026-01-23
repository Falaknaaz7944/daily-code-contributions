tasks = []

while True:
    print("\n--- TO-DO MENU ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("✅ Task added!")

    elif choice == "2":
        if not tasks:
            print("📭 No tasks yet")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🗑️ Removed: {removed}")
        else:
            print("❌ Invalid task number")

    elif choice == "4":
        print("👋 Exiting… Stay productive!")
        break

    else:
        print("⚠️ Choose a valid option")
