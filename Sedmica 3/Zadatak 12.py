import math

izbor = input("Unesite prirodan broj od 1 do 4: ")

if izbor == "1":
    r = float(input("Unesite poluprecnik kruga: "))
    print(f"Povrsina kruga: {(r**2)*math.pi} | Obim kruga: {math.pi*2*r}")

elif izbor == "2":
    a = int(input("Unesite prirodan broj a: "))
    b = int(input("Unesite prirodan broj b: "))
    print(f"Povrsina pravougaonika: {a*b} | Obim pravougaonika: {2*a+2*b}")

elif izbor == "3":
    a = float(input("unesite realan broj a: "))
    if a <= 0:
        print("Broj je negativan!")
    else:
        print(f"Povrsina kvadrata: {a**2}")

elif izbor == "4":
    a = int(input("Unesite cijeli broj a: "))
    b = int(input("Unesite cijeli broj b: "))
    if a > b:
        print("Broj a je veci od broja b!")
    elif b > a:
        print("broj b je veci od broja a!")
    else:
        print("Brojevi a i b su jednaki!")
else:
    print("Jedini validni izbori se nalaze u segmentu [1,4] gdje su odabiri brojeva iz skupa prirodnih brojeva!")
