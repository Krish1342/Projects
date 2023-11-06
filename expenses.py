
expenses = {}

while True:
    print("Expense Tracker Menu:")
    print("1. Add an expense")
    print("2. View expense summary")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        expense_name = input("Enter the name of the expense: ")
        expense_amount = float(input("Enter the amount: "))
        
        if expense_name in expenses:
            expenses[expense_name] += expense_amount
        else:
            expenses[expense_name] = expense_amount
        print(f"{expense_name} expense added.")
    
    elif choice == '2':
        print("Expense Summary:")
        for name, amount in expenses.items():
            print(f"{name}: Rs{amount}")
    
    elif choice == '3':
        break
    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

print("Goodbye!")
