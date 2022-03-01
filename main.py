import random
import time

print("Hi! Please choose number between 1 and 100")

time.sleep(1)

guess = int(input("enter the number: "))
correct_number = random.randint(1, 100)
time.sleep(1)

guess_count = 1
while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess < correct_number:
        guess = int(
            input("Wrong, try higher. enter the number : "))
    else:
        guess = int(
            input(
                "Wrong, try lower. enter the number : "))

print(f"Great! The number is {correct_number}. It took you {guess_count} tries")
time.sleep(10)