'''Genomför följande ändringar.

1. Fråga efter tal mellan 1 och 100 istället.
2. Översätt programmet till svenska!
3. Lägg till en ny variabel "antal_gissningar", som håller reda på hur många gissningar användaren behövde
för att hitta talet. Skriv ut hur många gissningar efteråt.

import random

n = random.randint(1,100)
print("Jag tänker på et nummer mellan 1 och 100. Gissa vilket?")

antal_gissningar = 0

while True:
    text = input("Din gissning: ")

    antal_gissningar += 1

    as_number = int(text)

    if as_number == n:
        print("Korrekt!")
        break

    if as_number < n:
        print("Fel, mitt nummer är högre...Försök igen!")

    if as_number > n:
        print("Fel, mitt nummber är lägre...Försök igen!")

print(f"Du behövde {antal_gissningar} gissningar.")'''

import random

n = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100. Guess which?")

antal_gissningar = 0


while True:
    text = input("Your guess: ")
    as_number = int(text)

    antal_gissningar += 1

    if as_number == n:
        print("Correct!")
        break

    if as_number < n:
        print("Wrong, my number is higher... Try again!")

    if as_number > n:
        print("Wrong, my number is lower... Try again!")

print(f"Du behövde {antal_gissningar} gissningar för att hitta talet.")
