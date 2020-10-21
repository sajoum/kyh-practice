'''Uppgift: Som en del i en polisutredning har ni fått i uppgift att hitta rader i
en loggfil som innehåller texten “BEAR” eller “X-RAY”.
Ladda ner bifogad fil, och skriv ett program som listar alla sådana rader. Vilken mening hittar ni?'''

'''filobjekt''' '''r innebär läsa fil'''

def read_file(file_name):
    f = open(file_name, 'r')
    return f

def find_words(f, keywords):

def main():
    f = read_file("system.log")
    f.close()

if __name__ == '__main__':
    main()