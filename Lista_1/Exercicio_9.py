
# Lista de exercícios I

#Exercício 9

#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

# Solicitar a quantidade de Km percorridos

a = float(input (f'Digite a quantidade de Km percorridos: '))


#Solicitar a quantidade de dias usados
b = float (input (f'Digite a quantidade de dias usados: '))

total = float (((60*b)+(0.15*a)))

# Exibir o valor a pagar

print()


print (f'O valor total a pagar é : R${total:.2f} ')

print ()


input ('Aperte qualquer tecla para sair')
