def validna_lozinka(s):
    validna = True
    malo = False
    veliko = False
    cifra = False
    nije_alnum = False
    spejs = False
    if len(s) < 10:
        return not validna
    else:
        for i in range(len(s)):
            if s[i].islower():
                malo = True
            elif s[i].isupper():
                veliko = True
            elif s[i].isnumeric():
                cifra = True
            elif not s[i].isalnum():
                nije_alnum = True
            elif s[i] == " ":
                spejs = True
        if malo and veliko and cifra and nije_alnum and (not spejs):
            return validna
        else:
            return not validna


print(validna_lozinka("Banana1;123"))
