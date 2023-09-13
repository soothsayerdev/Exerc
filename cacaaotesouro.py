# Resolucao pelo GPT

# Função para calcular a distância entre dois pontos (xa, ya) e (xb, yb)
def distance(xa, ya, xb, yb):
    return ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5

# Leitura das coordenadas da piscina
L, A = map(int, input().split())

# Leitura das coordenadas de Luan e Larissa
XA, YA = map(int, input().split())
XB, YB = map(int, input().split())

# Leitura das coordenadas da moeda
XM, YM = map(int, input().split())

# Cálculo das distâncias
dist_Luan = distance(XA, YA, XM, YM)
dist_Larissa = distance(XB, YB, XM, YM)

# Cálculo das probabilidades
prob_Luan = 1 / (1 + dist_Luan / dist_Larissa)
prob_Larissa = 1 / (1 + dist_Larissa / dist_Luan)

# Impressão das probabilidades com 6 casas decimais
print(f'{prob_Luan:.6f} {prob_Larissa:.6f}')
