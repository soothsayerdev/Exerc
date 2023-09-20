s = 0
num = int(input("Digite quantos numeros estaram na trilha de soma: "))

for i in range(0,num):
    n = int(input("Digite um numero: "))
    s += n 

print(f"O somatorio de todos o numero eh igual a {s}")
