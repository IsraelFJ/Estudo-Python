#estrutura condicional

idade = int (input('Digite sua idade: '))

if idade < 18:
    print("Você não pode acessar o evento ")
else:
    print('Você pode acessar o evento')

#Validar numero positivo ou negativo

numero = int (input('Digite um numero: '))
if numero > 0:
    print(f"Número {numero} é positivo")
elif numero < 0:
    print(f"Número {numero} é negativo")
else:
    print("Número é zero")

numero = float (input('Digite um numero: '))
if numero % 2 == 0:
    print(f"Numero {numero} é par")
elif numero % 2 != 0:
    print(f"Numero {numero} é impar")
else:
    print("Você digitou zero")