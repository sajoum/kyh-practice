'''12.1 Indentera koden så att programmet fungerar hos er!
12.2 Låt användaren skriva listan på studenter som en sträng, t.ex. "kalle,adam,eva" så att listan inte är hårdkodad i programmet
12.3 Ändra så namn skrivs ut med Stor Bokstav i början.
12.4 Ändra så att användaren matar in maxlängden på ett namn, och om det blir en ValueError exception så antas värdet "5" gälla

Tips: Googla eller kör help(..) i Python Console på följande:
  strip, title, split'''

def is_it_too_long(max_length, name):
    return len(name) > max_length

def main(max_length):
    students = input("Ange studenternas namn: ").split(',')

    for name in students:
        name = name.strip()
        if is_it_too_long(max_length, name):
            print(f"{name.title()} är för långt!")
        else:
            print(name)
if __name__ == '__main__':

    try:
        max_length = int(input("Ange namnens maixmala längd: "))
    except ValueError:
        max_length = 5
        print("Maxlängden är nu 5 ")
    main(max_length)

