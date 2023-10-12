a = input("Unesite vrijeme 1 (h min sec): ").split()
b = input("Unesite vrijeme 2 (h min sec): ").split()

a = [int(x) for x in a]
b = [int(x) for x in b]

# 14h = 50400s 15m = 900s 7s = 7s Total: 51307s
# 16h = 57600s 9m = 540s 34s = 34s Total: 58174s
# Razlika: 6867s

totala = (a[0] * 60 * 60) + (a[1] * 60) + a[2]
totalb = (b[0] * 60 * 60) + (b[1] * 60) + b[2]

totalc = abs(totala - totalb)

h = totalc / 60 / 60
m = (h - int(h)) * 60
s = round((m - int(m)) * 60)
h = int(h)
m = int(m)
s = int(s)
print("---------------------------------------------")
print("Izmedju ova dva trenutka je proteklo: ")
print(f"{h} h {m} min {s} sec.")
