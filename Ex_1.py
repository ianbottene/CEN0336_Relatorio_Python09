linhas = ["8.5", "abc", "11", "0", ""] #Cria uma lista com valores no formato str.

total = 0 #Cria a variável total e atribui o valor 0 a ela.
quantidade = 0 #Cria a variável quantidade e atribui o valor 0 a ela.
numero_linha = 0 #Cria a variável numero_linha e atribui o valor 0 a ela.

for linha in linhas: #Cria um loop for que percorre cada elemento da lista linhas.
    numero_linha += 1 #Incrementa a variável numero_linha em 1 a cada iteração do loop.

    try: #Tenta executar o bloco de código dentro do try.
        nota = float(linha.strip()) #Cria a variável nota e tenta converter a linha em um número float, para cada item da variável linhas.
        total += nota #Incrementa a variável total com o valor da nota.
        quantidade += 1 #Incrementa a variável quantidade em 1 a cada iteração do loop.
    except: #Caso o bloco try não seja executado, o bloco except será executado.
        print("Linha inválida") #Imprime uma mensagem de erro para linhas inválidas.
    else:
        if nota < 0 or nota > 10:
            raise ValueError("Nota fora do intervalo")

media = total / quantidade
print("Média:", media)
