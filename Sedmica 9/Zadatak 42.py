suma = 0
prethodni = ''

while True:
    n = int(input())
    if n == prethodni:
        break
    suma += n
    prethodni = n

print(f"Vasa suma je: {suma}")
