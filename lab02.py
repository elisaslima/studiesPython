###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Em Busca de um Chuveiro
# Nome: Ana Elisa da Silva Lima
# RA: 204409
###################################################

# Leitura da entrada
R = int(input())
V = int(input())
T = int(input())
C = float(input())
L = int(input())


# Cálculo do consumo e impressão da saída

# Equação da potência 
P = (V ** 2) // R

# Equação do consumo de energia
consumo = (P * T) // 1000

# Para descobrir o gasto total, basta multiplicar o consumo pelo custo do kWh
gastoTotal = consumo * C

# Testagem com L 
if gastoTotal <= L: 
    print(True)
else:
    print(False)