# Lista de exercícios I

#Exercício 5

#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

# Solicitar o valor da mercadoria

a = float(input (f'Digite o valor da Mercadoria em R$ :'))

# Solicitar o valor de desconto em %

b = float(input (f'Digite o valor do desconto em % :'))

# Exibir o salário com aumento

print()

print (f'O valor do desconto em R$  é : {(a*(b/100))}')

print ()

print (f'O valor da Mercadoria com desconto em R$  é : {a-(a*(b/100))}')

input ('Aperte qualquer tecla para sair')

