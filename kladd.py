import random

def ordlek():

    saker = ["En app", "En dammsugare", "En soffa"]
    sak = saker[random.randint(0, len(saker)-1)]
    kan_uttryck = random.choice(["laddas ner till mobiltelefonen", "skickas till månen", "levereras med lastbil"])
    grupp = random.choice(["finländare, stockholmare, amerikaner"])
    smitta = random.choice(["coronaviruset, pesten, resfeber"])
    person = random.choice(["Donald Trump, Påven"])
    yrkesroll = random.choice(["generaldirektör, butiksbiträde"])

    return f"""