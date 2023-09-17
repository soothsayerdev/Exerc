qt_numeros = int(input("Digite a quantidade de numeros a avaliar: "))
vet_nums = []
maior = 0
menor = 0

for i in range(0,qt_numeros):
    num = int(input("Digite os numeros: "))
    vet_nums.append(num)
    if i == 0:
        maior = menor = vet_nums[i]
    else:
        if vet_nums[i] > maior:
            maior = vet_nums[i]
        if vet_nums[i] < menor:
            menor = vet_nums[i]


print(f"O maior valor eh {maior} nas posicoes", end=" ")
for i, v in enumerate(vet_nums):
    if v == maior:
        print(f"{i} ...", end=" ")
print()
print(f"O menor valor eh {menor} nas posicoes", end=" ")
for i, v in enumerate(vet_nums):
        if v == menor:
            print(f"{i} ...", end=" ")
print()

    
