# CTI-110
# P4HW1 - Score List
# Kayla Young
# 11/12/2023

num_scores = input("How many scores do you want to enter? ")

# An empty list to input valid scores
score_list = []

# Create a loop to collect the number of scores 

for i in range(int(num_scores)):

    while True:
        # Ask the user to enter score
        score = input(f"Enter score #{i+1}:")
        
        # Check for the score to be valid then add to list
        if 0 <= float(score) <= 100:
            score_list.append(float(score))
            break
        else:
            # If it is not, ask for another score
            print("INVALID, please try again")

# Remove the lowest score from the list
lowest_score = min(score_list)
score_list.remove(lowest_score)

# Calculate the average of scores
average_score = sum(score_list) / len(score_list)

# Determine the letter grade 
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the results
print("--Results--")
print(f"Lowest Score: {lowest_score}")
print(f"Modified List: {score_list}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade: {letter_grade}")
