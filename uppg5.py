import random


n = random.randint(1, 100)
print("Jag tänker på ett nummer mellan 1 och 100. Gissa vilket?")
def ask_number():
    text = input("Din gissning: ")
    siffra = int(text)
    return siffra


def mainloop():
    antal_gissningar = 0
    while True:

        as_number = ask_number()

        antal_gissningar += 1



        if as_number == n:
            print("Korrekt!")
            return antal_gissningar

        if as_number < n:
            print("Fel, mitt nummer är högre... Försök igen!")

        if as_number > n:
            print("Fel, mitt nummer är lägre... Försök igen!")

antal_gissningar = mainloop()
print(f"Du behövde {antal_gissningar} gissningar.")







