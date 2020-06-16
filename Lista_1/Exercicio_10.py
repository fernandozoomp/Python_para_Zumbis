# Lista de exercícios I

#Exercício 10

#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

# Solicitar a quantidade de cigarros fumados em um dia

a = int(input (f'Digite a quantidade de cigarros fumados por dia: '))

# Solicitar a quantidade de anos que a pessoa fumou

b = int (input(f'Digite a quantidade de anos que fuma: '))

total = float ((((10*a)*(b*365))/1440))

# Exibir quanto tempo de vida o fumante já perdeu


print()



print(f'Você já perdeu {total:.0f} dias de vida')

print()

print('Digite uma tecla para sair')
