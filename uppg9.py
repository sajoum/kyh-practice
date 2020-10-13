'''9.1 Fixa så detta program fungerar igen.
9.2 Byt till f-string!
9.3 Gör så att programmet frågar efter antal uppgifter att lösa
9.4 Låt programmet fråga användaren vilket största talet ska vara'''
import random

def game(antal_uppgifter, max):
    correct_answers = 0
    for i in range(antal_uppgifter):
        a = random.randint(1, max)
        b = random.randint(1, max)
        answer = input(str(a) + "+" + str(b) + "=")
        number = int(answer)
        if number == a + b:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f"Fel... Det blir {a+b}")
            print("---")
    print(f"Du fick {correct_answers} av {antal_uppgifter} rätt.")

if __name__ == '__main__':
    number = int(input("Hur många uppgifter vill du lösa? "))
    max = int(input("Välj ett maxvärde: "))
    game(number, max)