# Simple To-Do List

tasks = []

while True:
    print("\n1.Add 2.View 3.Remove 4.Exit")
    choice = input("Choose: ")

    if choice == "1":
        tasks.append(input("Task: "))

    elif choice == "2":
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

    elif choice == "3":
        tasks.pop(int(input("Remove #: ")) - 1)

    elif choice == "4":
        break