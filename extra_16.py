def vowel(char):
    vowels = "aeiouy"
    if char.lower() in vowels:
        return True
    else:
        return False

def main():
    if vowel ("A"):
        print("Yes")
    else:
        print("No")

    if vowel ("B"):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
