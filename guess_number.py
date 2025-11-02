import random

target_number = random.randint(1, 10)

player_guess = int(input("Guess a number between 1 and 10: "))

while player_guess != target_number:
    if player_guess > target_number:
        print("Your number is greater than my number.")
    elif player_guess < target_number:
        print("Your number is less than my number.")
    
    player_guess = int(input("Try again: "))

print("🎉 Your guess is correct!")
