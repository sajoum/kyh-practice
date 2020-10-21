def translate(text):
    vowels = "aeiouy"

    rovarstring = ""
    for c in text:
        if c not in vowels and c.isalpha():
            rovarstring += c + "o" + c
        else:
            rovarstring += c

    return rovarstring

def main():
    print(translate("this is fun"))

if __name__ == '__main__':
    main()

