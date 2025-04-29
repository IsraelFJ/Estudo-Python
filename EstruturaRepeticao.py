# estrutura de repetiçao fomrato WHILE




# tabuada de adição
numero = int (input("Digite um numero: "))
x = 1
while x <= 10:
   print(numero+x)
   x = x+1


n = 1
soma = 0
while n <= 10:
    x = int (input("digite um numero: "))
    soma = soma + x
    n = n + 1
print(soma)


x = 1
while x <=10:
    if x == 5:
        break
print(x)
x= x + 1

x = 0
while True:
    num = int(input("digite um numero: "))
    if num == 0:
       break
    print(x)
    x = x + 1

for i in range(1,11):
    print(i)

for char in "phyton":
    print(char)

lista = [1,2,3,4,5,6,7,8,9]
for i in lista:
    print(i)