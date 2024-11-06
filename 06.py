lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]
lista = ["maria" if x == "joao" else x for x in lista ]
print(lista)