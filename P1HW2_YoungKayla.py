# This is a program to calculate and display the travel expenses
# 10/01/23
# CTI-110 P1HW2- Travel Expense
# Kayla Young

# Ask the user to enter their budget
budget = float(input("Enter Budget: "))

# Ask the user to enter the travel destination
destination = input("Enter your travel destination: ")

# Ask the user for the amount they will spend on gas
GasExpense = float(input("How much will spend on gas? "))

# Ask the user for the amount they will spend on accommodation
accommodation_expense = float(input("About how much do you think you'll spend on an accommodation?"))

# Ask the user for the amount they will spend on food
food_expense = float(input("Finally, how much do you think you'll need for food"))

# Add up the expenses
total_expenses = GasExpense + accommodation_expense + food_expense

# Subtract expenses from the budget
remaining_balance = budget - total_expenses

# Display the results
print("Location:", destination)
print("Initial Budget:", budget)
print("Fuel:", GasExpense)
print("Accommodation:", accommodation_expense)
print("Food:", food_expense)
print("Remaining Balance:", remaining_balance)
