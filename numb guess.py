
 
import random

def play_game():
    print("Choose difficulty: 1-Easy, 2-Medium, 3-Hard")
    choice = input("Enter 1, 2 or 3: ")

    if choice == '1':
        number = random.randint(1, 50)
        attempts = 10
    elif choice == '2':
        number = random.randint(1, 100)
        attempts = 7
    elif choice == '3':
        number = random.randint(1, 200)
        attempts = 5
    else:
        print("Invalid choice, defaulting to Medium.")
        number = random.randint(1, 100)
        attempts = 7

    print(f"\nGuess the number! You have {attempts}  attempts.")

    for i in range(attempts):
        
            guess = int(input(f"Attempt {i + 1}: "))
            if guess < number:
                print("Too low.")
            elif guess > number:
                print("Too high.")
            else:
                print(f"Correct! You guessed it in {i + 1} tries.")
                return
        

    print(f"Sorry, you ran out of attempts. The number was {number}.")

while True:
    play_game()
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        print("Goodbye!")
        break