 # Gives simple math quiz

   # 11/26/2023

   # CTI-110 P5HW - Math Quiz

   # Kayla Young

import random

def main():
    print("Welcome to Math Quiz")
    
    while True:
        display_menu()  
        choice = input("Please choose one of the  choices: ")

        if choice == "1":
            add_random_numbers()
        elif choice == "2":
            subtract_random_numbers()
        elif choice == "3":
            print("Thank you for participating...\nGoodbye!")
            break
        else:
            print("Invalid selection. Please select from the options below.")

def display_menu():
    print("MAIN MENU")
    print("1. Add Random Numbers")
    print("2. Subtract Random Numbers")
    print("3. Exit")

def add_random_numbers():
    num1 = random.randint(1, 100) 
    num2 = random.randint(1, 100) 
    correct_answer = num1 + num2  
    guess_count = 0                

    print(f"{num1: >3}\n+{num2: >2}\nEnter answer.")

    
    while True:
        guess = int(input())
        guess_count += 1
        if guess < correct_answer:
            print("Sorry, guess is not high enough.\nplease try again: ", end="")
        elif guess > correct_answer:
            print("Sorry, guess is not low enough.\nplease try again: ", end="")
        else:
            print("Congratulations that is correct.")
            print(f"Number of guesses: {guess_count}")
            break

def subtract_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 - num2
    guess_count = 0

    print(f"{num1: >3}\n-{num2: >2}\nEnter answer.")

    while True:
        guess = int(input())
        guess_count += 1
        if guess < correct_answer:
            print("Sorry, guess is not high enough.\nPlease try again: ", end="")
        elif guess > correct_answer:
            print("Sorry, guess is not low enough.\nPlease try again: ", end="")
        else:
            print("Congratulations that is correct.")
            print(f"Number of guesses: {guess_count}")
            break

if __name__ == "__main__":
    main()