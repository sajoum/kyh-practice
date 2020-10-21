'''
Feedback från användare av programmet:
 - Det behövs fler frågor!
 - Vi vill ha poäng!

Feedback från kollegor:
- Vi vill ha lite mer ordning och reda i program - det är massa dubbel kod!
Kan vi använda listor, dictionaries och/eller funktioner för att minska upprepningar i koden?
- Det känns dumt att hårdkoda frågorna/svaren i koden!
Kan vi lagra dem i en (eller flera) separata textfiler
(listor eller json eller vad ni vill som passar) som vi läser in när programmet startar?'''

questions = []
with open('questions.txt', encoding = 'utf-8') as f:
    for rad in f:
        question_row = rad.strip().split(',')
        question = question_row[0]
        right_answer = question_row[1]
        questions.append((question, right_answer))
points = 0
for question,right_answer in questions:
    ditt_svar = input(f'{question} ')
    if ditt_svar.lower() == right_answer.lower():
        points += 1
        print("Rätt!")
    else:
        print(f'Fel! Rätt svar är: {right_answer}')
print(f'Du fick {points} poäng av {len(questions)} möjliga.')

quit()

correct_answers = 0
question = "Vilken funktion används för att skriva ut saker på skärmen?"
right_answer = "print"
print(question)

answer = input("Ditt svar: ")

if answer == right_answer:
    print("Rätt!")
    correct_answers += 1
else:
    print(f"Fel! Rätt svar: {right_answer}")

question = "Vad skriver man för att avsluta programmet? "
right_answer = "break"
print(question)

answer = input("Ditt svar: ")

if answer == right_answer:
    print("Rätt!")
else:
    print(f"Fel! Rätt svar: {right_answer}")



'''Ex2'''

question = "Vad kallas en textharang i Python?"
right_answer = "sträng"
print(question)

answer = input("Ditt svar: ")

if answer == right_answer:
    print("Rätt!")
else:
    print(f"Fel! Rätt svar: {right_answer}")