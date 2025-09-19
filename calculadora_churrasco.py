# crie um programa que calcule a quantidade de bebida e de carne 
# para a organização de um churrasco 

# etapas da resolução 
#  
# 3) criara um função para calcular a quantidade total de carnes 
# 4) apresentar o resultado com os valores de total de carne e bebidas 
# a erem comprados 

# 1) solicitar o numero de convidados 
# usamos o int por qu convidados deve ser um numero inteiro 
convidados = int(input('digite o numero de convidados: '))

# 2) criar uma fumção para calular a quantidade total de bebidas 
def calcular_bebidas(convidados, consumo_por_pessoa_m =800, volume_garrafa_litro =2.25):
    total_m1 = convidados * consumo_por_pessoa_m # calcula o consumo de bebidas total por convidados/m1
    total_litro % volume =
#!)solicitar o numero de convidados
#2) criar uma funçao para calcular a quantidade total de bibeidas
#3) criar uma funçao pra calcular a quantidade total de carnes
#4) apresentar o resultado com os valores de total de carne e bebidas a serem compradsos

convidados=int(input('digite o numero de convidados: '))
def calcular_bebidas(convidados, consumo_por_pessoa_ml =800, volume_garrafa_litro =2.25):
    total_ml= convidados* consumo_por_pessoa_ml
    total_litro= total_ml/1000

# resultado=calcular_bebidas(convidados)
# print(resultado) 

def calcular_carne(convidados, consumo_por_pessoa_grama=400): 
    total_gramas = convidados * consumo_por_pessoa_grama # informa a quantidade total de carne em gramas 
    total_kg= total_gramas /1000 # Transformando o valor total em gamas para quilo
    return total_kg 

litros, grarrafas = calcular_bebidas(convidados)
carne_kg= calcular_carne(convidados)

print('/n__quantidade total para churrasco___')
print(f'numero de conviddos: {convidados}')
print(f'refrigerantes necessarios: {litros:.2f} litros.')
print(f'garrafas de 2,5L: {garrafas} unidades')
print(f'carne necessaria: {carne_kg:.2f} kg.')