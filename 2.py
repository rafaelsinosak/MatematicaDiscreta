def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

termos=0
while termos<=0:
    termos = int(input("Insira um numero pra fibonacci: "))
    if termos <= 0:
        print("Numero invalido")
print("Fibonacci:")
for i in range(termos):
       print("Nivel",i+1," ",recur_fibo(i))
