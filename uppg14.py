'''13.1 Utan att köra programmet längst ned i denna uppgift, beskriv vad det gör för varandra!
13.2 Modifiera programmet så att inte bara "kind" skrivs ut i write_things-funktionen, utan också antalet
things t.ex "CARS (3 st)"
13.3 Lägg till en ny kategori av saker till programmet, hitta på något! Och lägg i items av denna sort i en ny
lista, som skrivs ut på slutet.
13.4 Skriv ut items i alfabetisk ordning.
13.5 Låt användaren mata in innehåll i basket i form av en kommaseparerad sträng, t.ex.
kan användaren mata in "banana,apple, orange" och det tolkas som listan ["banana", "apple", "orange"]'''


FRUITS = ['banana', 'apple', 'orange']
CARS = ['volvo', 'ford', 'tesla']
ANIMALS = ['cat', 'dog', 'camel']

def run():
    basket = input("Add content in basket: ").split(',')

    cars = []
    fruits = []
    animals = []
    rest = []
    for item in basket:
        item = item.strip().lower()
        if item in CARS:
            cars.append(item)
        elif item in FRUITS:
            fruits.append(item)
        elif item in ANIMALS:
            animals.append(item)
        else:
            rest.append(item)
    write_things(cars, 'Cars')
    write_things(fruits, 'Fruits')
    write_things(rest, 'Misc')
    write_things(animals, 'Animals')

def write_things(items, kind):
    print(f"{kind.upper()} ({len(items)})")
    for item in sorted(items):
        print(f" {item}")


if __name__ == '__main__':
    run()
