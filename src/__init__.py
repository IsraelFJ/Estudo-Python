#entrada de dados


nome = input('Qual o seu nome? ')
idade = int (input('Qual a sua idade? '))
peso = float (input('Qual o seu peso? '))
print (f"{nome} tem {idade } e pesa {peso: .1f} kilos")


#variavel dentro da entrada de dados
nome = input('Qual o seu nome? ')
idade = int (input(f"Qual a sua idade {nome} ?"))
print(f"{nome} tem {idade} anos")

