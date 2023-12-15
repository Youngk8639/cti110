# CTI-110
# P2HW2 - List
# Kayla Young
# 10/23/23

grades = []
lowest_grade = float('inf')
highest_grade = float('-inf')
sum_of_grades = 0
for module in range(1, 7):
    grade = float(input(f"Enter grade for Module {module}: "))
    grades.append(grade)
    if grade < lowest_grade:
        lowest_grade = grade
    if grade > highest_grade:
        highest_grade = grade
    sum_of_grades += grade
average_grade = sum_of_grades / len(grades)
print("--------Results-----------")
print(f"Lowest Grade:      {lowest_grade:.1f}")
print(f"Highest Grade:      {highest_grade:.1f}")
print(f"Sum of Grades:      {sum_of_grades:.1f}")
print(f"Average:          {average_grade:.2f}")