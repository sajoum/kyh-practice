'''1. Skriv en funktion om "vänder" en textsträng baklänges - utan att använda "reverse"!
T.ex. "12345" blir "54321".'''


def reversed_text(text):
    rev_text = text[::-1] #[start:stop:step]
    return rev_text
alfabetet = "abcd efg"
text_backwards = reversed_text(alfabetet)
print(text_backwards)