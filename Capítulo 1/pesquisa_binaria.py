def pesquisa_binaria(lista, item):
    baixo = 0 
    alto = len(lista) - 1

    while baixo <= alto: #O laço continua enquanto não conseguir chegar a um único elemento
        meio = (baixo + alto) // 2 #Verifica o elemeto central
        chute = lista[meio] 
        if chute == item: #Verifica se o elemento central é igual o item
            return meio
        if chute > item: #Verifica seo chute foi muito alto
            alto = meio -1
        else: #Verifica se o chute foi muito baixo 
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9, 11, 13, 51]

print(pesquisa_binaria(minha_lista, 51))
print(pesquisa_binaria(minha_lista, -1))