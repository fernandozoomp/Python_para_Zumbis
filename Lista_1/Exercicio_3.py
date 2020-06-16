# Lista de exercícios I

#Exercício 3

#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

# Solicitar o valor do tempo

z = float (input ('Digite o valor dos dias: '))

a = float (input ('Digite o valor das horas: '))

b = float (input ('Digite o valor das minutos: '))

c = float (input ('Digite o valor das segundos: '))

#Apresentar o valor da soma em segundos

print()
print(f'O valor total em segundos é : {(z*24*3600)+(a*3600)+(b*60)+c}')
