###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Cupons de Desconto
# Nome: Ana Elisa da Silva Lima
# RA: 204409
###################################################

# Leitura de dados
X1 = float(input())
Z1 = float(input())
X2 = float(input())
Z2 = float(input())
X3 = float(input())
Z3 = float(input())
valorRecebido = float(input())


# Cálculo dos descontos
desconto1 = X1 if valorRecebido >= Z1 else 0

# O valor min é usado, pois para que o desconto X2 ocorra, é necessário que não se ultrapasse de um valor específico
desconto2 = min(X2 / 100 * valorRecebido, Z2)

desconto3 = X3 / 100 * valorRecebido if valorRecebido >= Z3 else 0

desconto = max(desconto1, desconto2, desconto3)

# Impressão da saída
maiorDesconto = []
if desconto == desconto1:
    maiorDesconto.append("1")
if desconto == desconto2: 
    maiorDesconto.append("2")
if desconto == desconto3: 
    maiorDesconto.append("3")

# A função len é utilizada para listas
if len(maiorDesconto) == 1:
    print("Maior desconto: Cupom", maiorDesconto[0])
else: 
    # A função join é utilizada, pois leva em consideração todos os itens que respeitam a condição proposta
    print("Maior desconto: Cupons", ", ".join(maiorDesconto))

# {:.2f} é um espaço reservado para um número de ponto flutuante com precisão de duas casas decimais e "format()" é usado para substituir os espaços reservados 
# replace()" é usado para substituir todos os pontos dados
print("Valor do desconto: R$ {:.2f}".format(desconto).replace(".", ","))