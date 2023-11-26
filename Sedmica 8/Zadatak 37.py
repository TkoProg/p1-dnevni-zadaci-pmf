def brojPojavljivanjaBroja(n, c):
    brojac = 0
    for i in range(1, n+1):
        if str(c) in str(i):
            brojac += 1
    return brojac


def ispisiPrveBrojeve(n, c):
    pojava = []
    i = 0
    brojac = 0
    while True:
        if brojac == n:
            return pojava
        if str(c) in str(i):
            pojava.append(i)
            brojac += 1
        i += 1


n = int(input("Unesite broj n: "))
c = int(input("Unesite broj c: "))

print("Broj pojavljivanja cifre c u raspoenu od 1 do n: ")
print(brojPojavljivanjaBroja(n, c))

print("Prvih n brojeva u kojim se nalazi cifra c: ")
[print(x, end=" ") for x in ispisiPrveBrojeve(n, c)]
