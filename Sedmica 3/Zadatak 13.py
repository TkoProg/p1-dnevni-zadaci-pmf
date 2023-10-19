a = float(input("Prvi broj: "))
b = float(input("Drugi broj: "))
c = float(input("Treci broj: "))

hip = max(a, b, c)

if c == hip:
    if c**2 == a**2 + b**2:
        print("Ovo je pravougli trugao.")
    else:
        print("Ovo nije pravougli trougao.")

elif b == hip:
    if b**2 == a**2 + c**2:
        print("Ovo je pravougli trugao.")
    else:
        print("Ovo nije pravougli trougao.")

if a == hip:
    if a**2 == c**2 + b**2:
        print("Ovo je pravougli trugao.")
    else:
        print("Ovo nije pravougli trougao.")
