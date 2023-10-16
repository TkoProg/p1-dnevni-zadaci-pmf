n = input("Unesite petocifren broj: ")
palindrom = True

for i in range(len(n)//2):
    if n[i] != n[len(n)-1-i]:
        palindrom = False
        break

if palindrom:
    print("Broj je palindrom!")
else:
    print("Broj nije palindrom!")
