budget = float(input("Enter your budget: ₦"))

expenses = []
add_more = "yes"
accepted_answer = ["yes","y","yeah","sure",]

while add_more in accepted_answer:
    amount = int(input("Enter the amount: "))
    category = input("Enter the category: ")
    description = input("Enter the description: ")

    expense = {
        "amount" : amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    add_more = input("Do you want to add another expense? ").lower()
for expense in expenses:
    print (f"amount : {expense['amount']}")
    print (f"category : {expense['category']}")
    print (f"description : {expense['description']}")
    print()


# Calculate total
total = 0

for expense in expenses:
    total += expense["amount"]

print(f"\nTotal expenses: ₦{total}")


# Compare with budget
while total > budget:
    print(f"You have ₦{budget - total} remaining.")


    remove_expense = input( "Would you like to remove an expense? ").lower()
        
    if remove_expense in ["yes", "y", "yeah", "yep"]:

        # Display expenses with numbers
        for index, expense in enumerate(expenses):
            print(
                f"{index + 1}. "
                f"{expense['category']} - "
                f"{expense['description']} - "
                f"₦{expense['amount']}"
            )
    
          

        # Get user's choice
        
    choice = int(input("Enter the number of the expense to remove: "))

           
                        
                # Check whether the choice is valid
    if 1 <= choice <= len(expenses):

                expense_index = choice - 1

                removed_expense = expenses[expense_index]

                expenses.pop(expense_index)

                total -= removed_expense["amount"]

                print("Expense removed successfully.")
                print(f"New total expenses: ₦{total}")
    else:
         break
        