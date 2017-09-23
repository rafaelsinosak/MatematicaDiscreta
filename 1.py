def menu(a):
    print("""1- Inserir os dois conjuntos (5 elementos cada)
2- Uniao dos conjuntos
3- Diferenca dos conjuntos
4- Soma dos conjuntos
5- Multiplicacao dos conjuntos
6- Intersecao dos conjuntos
7- Printar conjuntos
8- Limpar conjuntos
9- Sair""")
    while True:
        try:
            opcao = int(input())
            break
        except:
            print("Caracter invalido")
    while not 1 <= opcao <= 9:
        print("Opcao invalida")
        opcao = int(input())        
    else:
        return opcao

escolha=0
conj1=set()
conj2=set()
while True:
    escolha = menu(1)
    if escolha == 1:
        while True:
            try:
                for cont in range(5):
                    print "Conjunto 1, posicao",cont+1,": "
                    conj1.add(int(input()))
                    print "Conjunto 2, posicao",cont+1,": "
                    conj2.add(int(input()))
                break                
            except:
                print("Insira os conjuntos 1 2:")
    elif escolha == 2:
        if len(conj1)==0:  
            print("Insira os conjuntos")
        else:
            print("Uniao dos conjuntos 1 e 2: ", conj1.union(conj2))
    elif escolha == 3:
        if len(conj1)==0:  
            print("Insira os conjuntos!")
        else:
            print("Diferenca dos dois conjuntos 1 e 2 e: ", conj1.difference(conj2))
    elif escolha == 4:
        if len(conj1)==0:   
            print("Insira os conjuntos")
        else:
            print("Soma dos conjuntos: ", [x+y for x, y in zip(list(conj1),list(conj2))])
    elif escolha == 5:
        if len(conj1)==0: 
            print("Insira os conjuntos")
        else:
            print("Multiplacacao dos conjuntos: ", [x*y for x, y in zip(list(conj1),list(conj2))])
    elif escolha == 6:
        if len(conj1)==0:   
            print("Insira os conjuntos")
        else:
            print("Intersecao dos conjuntos 1 e 2: ", conj1.intersection(conj2))
    elif escolha == 7:
        if len(conj1)==0:  
            print("Insira os conjuntos")
        else:
            print("Conjunto 1: ",conj1,"Conjunto 2: ",conj2)
    elif escolha == 8:
        if len(conj1)==0:    
            print("Insira os conjuntos")
        else:
            conj1.clear()
            conj2.clear()
            print("Conjuntos vazios")
    else:
        break
