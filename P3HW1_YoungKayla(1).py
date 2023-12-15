# I was supposed to put a comment here
# My Last Name
# This program takes a number grade , determines average and displays letter grade for average.
# Enter grades for six modules

mod1 = input('Enter grade for Module 1: ')
mod2 = input('Enter grade for Module 2: ')
mod3 = input('Enter grade for Module 3: ')
mod4 = input('Enter grade for Module 4: ')
mod5 = input('Enter grade for Module 5: ')
mod6 = input('Enter grade for Module 6: ')

# add grades entered to a list

grades = [mod1, mod2, mod3, mod4, mod5, mod6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = high(grades)
sum = sum(grades)
avg = avg(grades)

# determine letter grade for average

print("------Results---------")
print("Lowest Grade: %.2f"%low)
print("Highest Grade: %.2f"%high)
print("Sum of Grades: %.2f"%sum)
print("Average: %.2f"%low)
print("--------------------")

if avg >= 90:
    print("Your grade is: A")
# elif is used not else if 
elif avg > 80:
    print("Your grade is: B")
elif avg > 70:
    print("Your grade is: C")
elif avg > 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")


