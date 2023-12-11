def dekompresuj(l):
    nova = []
    broj = 0
    for i in range(len(l)):
        if i % 2 == 0:
            broj = l[i]
        else:
            broj_ponavljanja = l[i]
            for i in range(broj_ponavljanja):
                nova.append(broj)
    return nova


print(dekompresuj([1, 1, 2, 3]))
