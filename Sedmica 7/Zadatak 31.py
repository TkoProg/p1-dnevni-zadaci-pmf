import random

a = random.randint(1, 999)
b = random.randint(1, 999)

operacija = random.randint(1, 4)

print(f"Generisani broj a: {a}")
print(f"Generisani broj b: {b}")

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
    print(f"a + b = {rezultat}")
elif operacija == 2:
    rezultat = a - b
    print(f"a - b = {rezultat}")
elif operacija == 3:
    rezultat = a * b
    print(f"a * b = {rezultat}")
else:
    rezultat = a // b
    print(f"a // b = {rezultat}")
