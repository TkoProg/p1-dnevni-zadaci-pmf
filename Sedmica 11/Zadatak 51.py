import random

sluc = random.randint(1000, 9999)

sluc = list(str(sluc))

while True:
    pogodjene = []
    n = input("Unesite cetverocifren broj: ")
    n = list(n)
    brojac  = 0
    if n == sluc:
        print("Pogodili ste cifru!")
        break
    for i in range(4):
        if n[i] == sluc[i]:
            brojac += 1
    pojavljuje = 0
    for i in range(4):
        if n[i] in pogodjene:
            continue
        if n[i] in sluc:
            pojavljuje += 1
            pogodjene.append(n[i])
    print(f"Broj cifara koji ste podili: {pojavljuje}")
    print(f"Broj cifara na pravom mjestu je: {brojac}")
