# Travel expense budget
# 10/19/2023
# CTI-110 P2HW1 - Travel
# Kayla Young

# User input
Budget = float(input("Enter Budget: "))
Destination = input("Enter your travel destination: ")
Gas = float(input("How much do you think you will spend on gas? "))
Accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food_ex = float(input("Last, how much do you need for food? "))

# Calculate total travel expenses
total_travel_expenses=gas_ex+accommodation_ex+food_ex

# Calculate remaining balance
remaining_balance=budget-(gas+accommodation+food)

# Display the travel expenses
print("\nTravel Expenses:")
print("Location:", destination)
print("Initial Budget:", "${:.2f}".format(budget))
print("Fuel:", "${:.2f}".format(gas_expenses))
print("Accommodation:", "${:.2f}".format(accommodation_expenses))
print("Food:", "${:.2f}".format(food_expenses))
print("Remaining Balance:", "${:.2f}".format(remaining_balance))