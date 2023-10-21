def povrsina(x11, x21, x31, y11, y21, y31):
    return 1/2 * abs(x11 * (y21 - y31) + x21 * (y31 - y11) + x31 * (y11 - y21))


x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
x3 = float(input("x3: "))
y3 = float(input("y3: "))

eps = 0.00000001

P1 = povrsina(x1, x2, x3, y1, y2, y3)

if P1 == 0:
    print("Tacke su kolinearne!")

else:
    x4 = float(input("x4: "))
    y4 = float(input("y4: "))

    P2 = povrsina(x1, x2, x4, y1, y2, y4)
    P3 = povrsina(x2, x3, x4, y2, y3, y4)
    P4 = povrsina(x1, x4, x3, y1, y4, y3)

    if P1 - eps < P2 + P3 + P4 < P1 + eps:
        print("Tacka se nazali u trouglu!")
    else:
        print("Tacka se ne nalazi u trouglu!")
