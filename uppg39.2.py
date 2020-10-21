'''2. Skriv en funktion som summerar alla tal i en lista. Inbyggda funktionen sum() ska ej användas'''

integers = [1,2,3]
def calculate_sum(integers):
    summa = 0
    for tal in integers:
        summa += tal
    return summa

summation = calculate_sum(integers)
print(summation)

summation2 = calculate_sum([3,5,7])
print(summation2)

summation3 = calculate_sum([2,2,2])
print(summation3)
