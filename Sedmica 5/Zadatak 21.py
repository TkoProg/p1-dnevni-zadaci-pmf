import random

brojac = 0

while True:
    novcic = int(input("Bacite novcic (0 = glava | 1 = pismo): "))
    if novcic == random.randint(0,1):
        print("Pogodili ste!")
        brojac += 1
    else:
        break

print(f"Broj tacnih pogodaka kojih ste imali je: {brojac}")
