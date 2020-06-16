# Lista de exercícios I

#Exercício 4

#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

# Solicitar o valor do salário

a = float(input (f'Digite o valor do Sálario em R$ :'))

# Solicitar o valor do aumento

b = float(input (f'Digite o valor do Aumento em % :'))

# Exibir o salário com aumento

print()

print (f'O valor do salário em R$ com aumento é : {(a*(b/100))+a}')

print ()


input ('Aperte qualquer tecla para sair')
