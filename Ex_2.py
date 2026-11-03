lista = ["0", "3", "abc"]

quantidade = len(lista)
total = 0
print(quantidade)

for n in lista:
    try:
        nota = float(n.strip())
        total += nota
    except: 
        print("Linha inválida")

media = total/quantidade
print(nota)

print("Média:", media)