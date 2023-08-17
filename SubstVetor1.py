vet = []

for i in range(3):
    num = int(input("Digite um Numero:"))
    vet.append(num)


for i in range(3):
    if vet[i] < 1:
        vet[i] = 1
        

for i in range(3):
    print(f"X[{i}] = {vet[i]}")
        
        