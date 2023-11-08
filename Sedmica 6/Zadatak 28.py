n = int(input("Unesite prirodan broj n: "))

suma = 0

for i in range(n):
    a = input(f"Unesite {i+1}. broj: ")
    suma = int(a[0]) + suma

print(f"Vas zbir je {suma}.")
