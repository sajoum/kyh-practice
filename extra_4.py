
char = input("Write a character: ")
vowels = "aeiouy"

if char.lower() in vowels:
    print(f"The entered letter {char} is a vowel")
else:
    print(f"Letter {char} is not a vowel")