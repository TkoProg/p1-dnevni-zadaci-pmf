s = int(input("Unesite PIN broj od 4 cifre: "))

if 999 < s < 10000:
    print("""1. Pregled stanja
2. Uplata
3. Isplata
4. Izlaz""")
    o = input("Unesite opciju: ")
    if o == "1":
        print("Imate 8550KM")
    elif o == "2":
        u = int(input("Koliko zelite uplatiti (moguce od 0KM do 2000KM): "))
        if 0 <= u <= 2000:
            u1 = input("Zelite li da vidite trenutno stanje? ('D' ili 'N'): ")
            if u1 == "D":
                print(f"Trenutno stanje je: {8550 + u}")
            elif u1 == "N":
                print("Hvala na koristenju nasih usluga!")
        else:
            print("Nemoguca uplata!")
    elif o == "3":
        i = int(input("Koliko zelite isplatiti (moguce od 0KM do 500KM, i vrijednost mora biti djeljiva sa 100): "))
        if i % 100 == 0 and 0 <= i <= 500:
            print(f"Trenutno stanje je: {8550 - i}")
        else:
            print("Nemoguca isplata!")
    elif o == "4":
        print("Hvala na koristenju nasih usluga!")
    else:
        print("Netacan odabir opcije!")
else:
    print("PIN mora biti tacno 4 cifre!")
