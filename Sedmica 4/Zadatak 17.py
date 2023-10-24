n = int(input("Unesite broj, program ispituje da li je broj super ili ne: "))

if n % 2 == 0 or n % 3 == 0:
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 3 == 0:
            n = n / 3
        else:
            print("Broj nije super!")
            break
    if n == 1:
        print("Broj je super!")
elif n == 1:
    print("Broj je super!")
else:
    print("Broj nije super!")
