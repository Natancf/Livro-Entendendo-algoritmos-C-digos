def fat(x): #função/pilha de chamada
    if x == 1: #caso-base
        return 1
    else: # caso recursivo
        return x * fat(x-1) #chamada da função, recursão

print(fat(3))

#outro exemplo

def sauda(nome):
    print(f"Olá {nome}!")
    sauda2(nome)#recursão
    print("preparando para dizer tchau...")
    tchau()#recursão
def sauda2(nome):
    print(f"Como vai {nome}?")
def tchau():
    print("ok, tchau!")
sauda("natan")