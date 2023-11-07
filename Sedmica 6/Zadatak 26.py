import math

brojac = 0
naj = 1

while True:
    n = int(input("Unesite prirodan broj: "))
    if n == 1:
        break
    if brojac == 0:
        naj = n
        brojac += 1
    naj = math.gcd(n, naj)

print("----------------------------")

print(f"NZD je {naj}.")
