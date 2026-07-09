total = 0

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Show Total")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        expense = float(input("Enter expense amount: "))
        total = total + expense
        print("Expense added successfully!")

    elif choice == "2":
        print(f"Total Spent: ₹{total}")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")