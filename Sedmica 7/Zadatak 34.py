# Stvarno mi je mrsko uraditi ovaj zadatak, bukvalno imam ispite a prevelika je pegla, iako je lagano.

import random

brojac = 0

print("---------------------------")
print(f"Milijunas: Random matematicka operacija verzija!")
print("---------------------------")

while True:
    a = random.randint(1, 999)
    b = random.randint(1, 999)

    operacija = random.randint(1, 4)

    if operacija == 1:
        o = "+"
    elif operacija == 2:
        o = "-"
    elif operacija == 3:
        o = "*"
    else:
        o = "//"

    print(f"Generisana operacija: '{o}'")

    print("---------------------------")

    if operacija == 1:
        rezultat = a + b
        rez1 = random.randint(a, a + 20 * b)
        rez2 = random.randint(a, a + 40 * b)
        rez3 = random.randint(a, a + 30 * b)
        rez = []
        pojava = []
        while True:
            broj = random.randint(0, 3)
            if broj in pojava:
                continue
            if broj == 0:
                rez.append(rez1)
            elif broj == 1:
                rez.append(rez2)
            elif broj == 2:
                rez.append(rezultat)
            else:
                rez.append(rez3)
            pojava.append(broj)
            if len(pojava) == 4:
                break
        for i in range(len(rez)):
            print(f"{i+1}. broj: {rez[i]}")
        pitanje = int(input("Koji je odgovor? (Redni broj): "))
        if rezultat == rez[pitanje-1]:
            print("Pogodili ste tacno!")
            brojac += 1
        else:
            print("Niste pogodili...")
            break
    elif operacija == 2:
        rezultat = a - b
        rez1 = random.randint(a, a + a * b)
        rez2 = random.randint(a, a + b * b)
        rez3 = random.randint(a, a + a * b)
        rez = []
        pojava = []
        while True:
            broj = random.randint(0, 3)
            if broj in pojava:
                continue
            if broj == 0:
                rez.append(rez1)
            elif broj == 1:
                rez.append(rez2)
            elif broj == 2:
                rez.append(rezultat)
            else:
                rez.append(rez3)
            pojava.append(broj)
            if len(pojava) == 4:
                break
        for i in range(len(rez)):
            print(f"{i + 1}. broj: {rez[i]}")
        pitanje = int(input("Koji je odgovor? (Redni broj): "))
        if rezultat == rez[pitanje - 1]:
            print("Pogodili ste tacno!")
            brojac += 1
        else:
            print("Niste pogodili...")
            break
    elif operacija == 3:
        rezultat = a * b
        rez1 = random.randint(a, a * 2 * b)
        rez2 = random.randint(a, a * 4 * b)
        rez3 = random.randint(a, a * 3 * b)
        rez = []
        pojava = []
        while True:
            broj = random.randint(0, 3)
            if broj in pojava:
                continue
            if broj == 0:
                rez.append(rez1)
            elif broj == 1:
                rez.append(rez2)
            elif broj == 2:
                rez.append(rezultat)
            else:
                rez.append(rez3)
            pojava.append(broj)
            if len(pojava) == 4:
                break
        for i in range(len(rez)):
            print(f"{i + 1}. broj: {rez[i]}")
        pitanje = int(input("Koji je odgovor? (Redni broj): "))
        if rezultat == rez[pitanje - 1]:
            print("Pogodili ste tacno!")
            brojac += 1
        else:
            print("Niste pogodili...")
            break
    else:
        a1 = max(a, b)
        b1 = min(a, b)
        rezultat = a1 // b1
        rez1 = random.randint(4, 5)
        rez2 = random.randint(6, 7)
        rez3 = random.randint(8, 10)
        rez = []
        pojava = []
        while True:
            broj = random.randint(0, 3)
            if broj in pojava:
                continue
            if broj == 0:
                rez.append(rez1)
            elif broj == 1:
                rez.append(rez2)
            elif broj == 2:
                rez.append(rezultat)
            else:
                rez.append(rez3)
            pojava.append(broj)
            if len(pojava) == 4:
                break
        for i in range(len(rez)):
            print(f"{i + 1}. broj: {rez[i]}")
        pitanje = int(input("Koji je odgovor? (Redni broj): "))
        if rezultat == rez[pitanje - 1]:
            print("Pogodili ste tacno!")
            brojac += 1
        else:
            print("Niste pogodili...")
            break

print("---------------------------")
print(f"Tacno ste odgovorili na {brojac} pitanja!")
print("---------------------------")
