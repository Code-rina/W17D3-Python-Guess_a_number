import random

guesses = 0 
name = input("What's your name?")
print(name)
num = random.randint(0, 10)
print("Guess a number between 1 and 20")

while guesses < 6:
    print("Please, take a guess")
    user_input = int(input('Guess: '))
    guesses += 1
    if user_input < num:
        print("Your guess is too low.")
    elif user_input > num:
        print("Your guess is too high.")
    elif user_input == num:
        break

if user_input == num:
        print(f"Good job {name}! You guessed the number in {guesses} guesses!")
elif user_input != num:
        print(f"Sorry, {name}. You could not guess my number {guesses}.")   

