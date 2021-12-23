def buscaMenor(arr):
    menor = arr[0] #guarda o menor valor
    menor_indice = 0 #guarda o indice do menor valor
    for i in range(1, len(arr)):
        if arr[i] < menor: #verifica qual é o menor valor é o coloca na variavel menor
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporselecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr) #encontra qual é o menor elemento do array e o adiciona no novo array
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoporselecao([5, 3, 6, 2, 10]))