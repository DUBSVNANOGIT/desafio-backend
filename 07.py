count = 0
lista = [0, 1, 2, 3, 4, 5]
while count < len(lista):
    if lista[count] <= 5:
        print(lista[count])
        lista[count] = lista[count] + 1
    count += 1