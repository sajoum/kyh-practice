'''Vi har gått igenom funktioner i teorin, nu blir det praktik!

1. Ändra så att hela while-loopen ligger i en funktion som heter "mainloop", och testa så att programmet fungerar fortfarande.
2. Bygg en funktion "ask_number" som returnerar ett heltal som användaren matar in.
3. Ändra på mainloop så att den returnerar antal gissningar användaren använt sig av, och skriv ut antalet utanför mainloop, inte  inuti.'''

import random

n = random.randint(1, 100)
print("Jag tänker på ett tal mellan 1 och 100. Gissa vilket?")


def mainloop():
    antal_gissningar = 0

    while True:
        as_number = ask_number()
        antal_gissningar += 1

        if as_number == n:
            print("Korrekt!")
            break

        if as_number < n:
            print("Fel, mitt tal är högre...Försök igen!")

        if as_number > n:
            print("Fel, mitt tal är lägre...Försök igen!")

    return antal_gissningar

def ask_number():
    text = input("Din gissning: ")
    as_number = int(text)
    return as_number

gissningar = mainloop()

print(f"Du behövde {gissningar} gissningar för att finna det rätta svaret")

