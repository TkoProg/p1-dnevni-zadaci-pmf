import math as m

a = float(input())
a = m.radians(a)
n = float(input())
k = float(input())
h = float(input())

print(((2 * m.pow(k, 2/3)) * m.cos(a)) / (m.sin(a) * m.sqrt(h+n)))
