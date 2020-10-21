import random

n = random.randint(1, 3)
print("Jag tänker på ett nummer mellan 1 och 10. Gissa vilket?")

'''Bygg en funktion "ask_number" som returnerar ett heltal som användaren matar in.'''
def ask_number():
    text = input("Din gissning: ")
    heltal = int(text)
    return heltal

def mainloop():
    antal_gissningar = 0
    while True:
        as_number = ask_number()

        antal_gissningar += 1

        if as_number == n:
            print("Korrekt!")
            break

        if as_number < n:
            print("Fel, mitt nummer är högre... Försök igen!")

        if as_number > n:
            print("Fel, mitt nummer är lägre... Försök igen!")
    return antal_gissningar

if __name__ == "__main__":
    antal_gissningar = mainloop()
    print(f"Du behövde {antal_gissningar} gissningar.")