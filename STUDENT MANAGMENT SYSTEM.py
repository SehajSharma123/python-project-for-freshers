students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = input("Roll No: ")
        name = input("Name: ")
        students[roll] = name
        print("Student Added")

    elif choice == 2:
        print("Student Records:")
        for r, n in students.items():
            print(r, ":", n)

    elif choice == 3:
        roll = input("Enter roll to delete: ")
        students.pop(roll, None)
        print("Student Deleted")

    elif choice == 4:
        break
