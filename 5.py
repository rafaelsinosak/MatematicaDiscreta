def primo(num):
    if (num<=1):
        return False
    for n in range (1,num):
        if (num%n==0 and n!=1 and n!=num):
            return False
    else:
        return True
    
primos=[]
nprimos=[]
num=input("Entre com o numero: ")
for x in range(num+1):
    print x,"e primo? ", primo(x)
    if (primo(x)==True):
        primos.append(x)
    else:
        nprimos.append(x)
print ("\nConjunto dos numeros primos: "+str(primos))
print ("\nConjunto dos numeros que nao sao primos: "+str(nprimos))
