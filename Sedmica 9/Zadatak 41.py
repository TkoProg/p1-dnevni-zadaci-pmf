import math


def jelProst(n):
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


prost = 0
prethodni = ""

while True:
    n = int(input())
    if n == prethodni:
        break
    if jelProst(n):
        prost = n
    prethodni = n

if prost == 0:
    print("Niste unijeli prost broj! Vas rezultat je 0!")
else:
    print(f"Najveci uneseni prosti broj je: {prost}!")
