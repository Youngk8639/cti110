# CTI-110
# P3HW2 - Salary
# Kayla Young
# 10/23/23

# Pseudocode:
# The employee's name (John Smith)
# Number of hours worked (45)
# Pay rate from (17.5)
# See if the employee has worked overtime(More than 40)
# Calculate the amount owed for overtime hours, regular hours and gross pay
# Display the employee name, payrate, hours worked, overtime hours, overtime pay, pay for regular hours, and gross pay.


employee_name = input("Enter the name of the employee: ")

# The number of hours worked
hours_worked = float(input("Enter the number of hours worked this week: "))

# Employee's pay rate
pay_rate = float(input("Enter the employee's pay rate: "))

# Overtime houts
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overTime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

# Pay calculated
gross_pay = regular_pay + overTime_pay

# Display the results
print("Employee Name:", employee_name)
print()
print("Hours Worked \t Pay Rate \t OverTime \t OverTimePay \t RegHour Pay \t Gross Pay")
print("-"*80)
print(hours_worked," \t\t ",pay_rate," \t ",overtime_hours," \t\t ",overTime_pay," \t  ",regular_pay," \t ",gross_pay)