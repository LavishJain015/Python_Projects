import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎮 Number Guessing Game")
print("Guess the number between 1 and 100")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"🎉 Correct! You won in {attempts} attempts.")
        break