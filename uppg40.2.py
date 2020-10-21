'''2. Skriv en funktion som tar in en textsträng, och returnerar antalet stora bokstäver i strängen.'''

def check_no_uppercase(text):
    no_of_uppercase = 0
    for letter in text:
        if letter.isupper():
            no_of_uppercase += 1
    return no_of_uppercase
