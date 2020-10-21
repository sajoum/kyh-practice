import random

def ordlek():

    saker = ["En app", "En dammsugare", "En soffa"]
    sak = saker[random.randint(0, len(saker)-1)]
    kan_uttryck = random.choice(["laddas ner till mobiltelefonen", "skickas till månen", "levereras med lastbil"])
    grupp = random.choice(["finländare", "stockholmare", "amerikaner"])
    smitta = random.choice(["coronaviruset", "pesten", "resfeber"])
    person = random.choice(["Donald Trump", "Påven"])
    yrkesroll = random.choice(["generaldirektör", "butiksbiträde"])

    return f"""
{sak} som kan {kan_uttryck} ska varna
{grupp} som kommit nära någon som smittats med {smitta}.
- Jag tycker ni i Sverige borde överväga att göra något
liknande, säger {person}, {yrkesroll} för
Finska institutet för hälsa och välfärd, THL."""

if __name__ == '__main__':

    text = ordlek()

    print(text)