'''10. Skriv flera program (t.ex ug10_1.py, ug10_2.py osv) som skriver ut:
1) heltalen fr.o.m. 1 t.o.m. 10 i ökande ordning
2) udda tal fr.o.m. 1 t.o.m. 49 i ökande ordning
3) heltal fr.o.m. 10 t.o.m. 1 i minskande ordning
4) summan av talen 7 t.o.m 1000
5) produkten av talen 1 t.o.m 1000'''

for i in range (1, 11):
    print (i)

for i in range(1, 50):
        print(i)

for i in range(1, 50):
            print(i)

for i in range(1, 50):
                print(i)


for i in range(10, 0, -1):
                print(i)


total = 0
for i in range(7, 1001):
    total = total + i
print(total)


total = 0
for i in range(1, 1001):
    total = total * i
print(total)

