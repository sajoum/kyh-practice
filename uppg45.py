'''
15.1 Implementera "wordcount" som jag och Christoffer byggde
15.2 Ta in en godtycklig text (testa att copy-paste från lorumipsum.com) och skriv ut hur många vokaler som finns i strängen.
Tips: "a" in "abcd" är True!
15.3 Göteborgsvarvet, vilken placering kom XYZ på? Implementera resten av detta program:
    runners_in_order = “Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus”.split()
    vem = input(“Ange löpare du söker placering för”)'''

def wordcount(text):
    # 1. Dela texten i mellanrum (med split)
    # 2. Beräkna längden på resultatlistan
    # 3. Profit
    return len(text.split())


if __name__ == '__main__':
    text = input("Skriv in en text: ")
    print("I den texten hittade jag {:20} ord. Byeeee!".format(wordcount(text)))
    print("I den texten hittade jag %s ord. Byeeee! "%(wordcount(text)))
    print(f"I den texten hittade jag {wordcount(text):20} ord. Byeeee! ")

text = "Ta in en godtycklig text (testa att copy-paste från lorumipsum.com"
vokaler = ["a", "e", "i", "o", "u"]
antal_vokaler = 0
for letter in text.lower():
    if letter in vokaler:
        antal_vokaler += 1
print(f'antal vokaler: {antal_vokaler}')

runners_in_order = "Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus".split()
vem = input("Ange löpare du söker placering för: ")

position = runners_in_order.index(vem) + 1
print(f'{vem} kom på {position} plats. ')

