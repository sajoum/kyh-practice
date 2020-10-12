'''Genomför följande ändringar.
1. Fråga efter tal mellan 1 och 100 istället.
2. Översätt programmet till svenska!
3. Lägg till en ny variabel "antal_gissningar", som håller reda på hur
många gissningar användaren behövde för att hitta talet. Skriv ut hur många gissningar efteråt.'''

import random

n = random.randint(1, 100)
print("Jag tänker på ett tal mellan 1 och 100. Gissa vilket?")

antal_gissningar = 0

while True:
    text = input("Din gissning: ")
    as_number = int(text)

    if as_number == n:
        print("Korrekt!")
        break

    if as_number < n:
        print("Fel, mitt tal är högre...Försök igen!")

    if as_number > n:
        print("Fel, mitt tal är lägre...Försök igen!")

    antal_gissningar += 1

print("Du behövde " + str(antal_gissningar) + " gissningar för att finna det rätta svaret")

