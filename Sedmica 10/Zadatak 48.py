def sortiranje_liste(l):
    nova = []
    for i in range(len(l)):
        najveci = -1
        for j in range(i+1, len(l)):
            if l[j] >= najveci:
                najveci = l[j]
        nova.append(najveci)
    return nova


print(sortiranje_liste([17, 18, 5, 4, 6, 1]))
