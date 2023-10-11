import random as rnd
def calcula_media(v):
    """
    Função que calcula a média dos valores de uma lista
    """
    if len(v) > 0:
        return sum(v)/len(v)
    else:
        return 0
    
def inicializa_lista(quantidade=5):
    lista = []
    for _ in range (quantidade):
        valor = rnd.randint(0,100)
        lista.append(valor)
        return lista    
       
def menu():
    print ("=" *40)
    print ("1- Iniciar lista aleatória")
    print ("2- Calcular média")
    print ("3- Pesquisar valor")
    print ("4- Sair")
    return int(input("Digite sua opção: "))

def pesquisar():
    pesquisa = int(input("Digite o número que deseja pesquisar: "))
    return pesquisa in v
           
if __name__=='__main__':
    v = []
    opcao = 0   
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            v = inicializa_lista()
            print (v)

        if opcao == 2:
            media = calcula_media(v)
            print(f"A média é {media:.2f}")
        if opcao == 3:
            pesquisa = pesquisar()
            if pesquisa == True:
                print("Está presente")
            else:
                print("Não está presente")
    else:
        print ("Saindo ...")


