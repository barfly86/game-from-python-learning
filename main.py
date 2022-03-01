import random
import time

print("Cześć! Zgadnji ukrytą liczbę pomiędzy 1 a 100")

time.sleep(1)

guess = int(input("podaj liczbę: "))
correct_number = random.randint(1, 100)
time.sleep(1)

guess_count = 1
while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess < correct_number:
        guess = int(
            input("zła odpowiedź, podana liczba jest większa. podaj liczbę: "))
    else:
        guess = int(
            input(
                "zła odpowiedź, podana liczba jest mniejsza. podaj liczbę: "))

print(f"BRAWO! ukryta liczba to {correct_number}.")