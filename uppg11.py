'''11.1 Ta en kopia på uppgift 9 och fixa programmet så att int(input(..)) inte kraschar om användaren skriver "abc" (tips: använd try...except  block!)
11.2 Fortsätt jobba med det ni inte blev klara med i uppgift 9, 10
11.3 Jobba med extrauppgifter'''


import random

def game(number_of_questions, max_value):
    correct_answers = 0
    for i in range(number_of_questions):
        a = random.randint(1, max_value)
        b = random.randint(1, max_value)
        answer = input(str(a) + "+" + str(b) + "=")
        number = int(answer)

        if number == a + b:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f"Fel... Det blir {a+b}")
            print("---")
    print(f"Du fick {correct_answers} av {number_of_questions} rätt.")

if __name__ == '__main__':
    try:
        number = int(input("Hur många frågor? "))
        max_value = int(input("Största tal? "))
        game(number, max_value)
    except:
        print("Oj, här blev det fel!")


