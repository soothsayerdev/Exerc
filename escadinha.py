num = int(input("Digite um numero para estar na escadinha: "))
trilha = []

for i in range(1,num + 1):
    trilha.append(num - 1)
    print(trilha)


for i in range(1,num + 1):
    trilha.append(num - 1)
    num -= 1
    print(trilha)