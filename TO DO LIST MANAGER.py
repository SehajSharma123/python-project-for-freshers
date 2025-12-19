todo = []

while True:
    print("\n1.Add 2.View 3.Exit")
    ch = int(input("Choose: "))

    if ch == 1:
        todo.append(input("Task: "))
    elif ch == 2:
        print(todo)
    elif ch == 3:
        break
