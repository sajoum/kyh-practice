def reversed_text(text):
    new_text = ""
    for letter in text:
        new_text = letter + new_text
        print(new_text) #för att se hur bokstäverna läggs till# "Bra vid tex felsök, koden funkar även om rad 5 raderas#
    return new_text



alfabetet = "abcdefghi"
text_backwards = reversed_text(alfabetet)
print(text_backwards)