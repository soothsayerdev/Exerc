n_testes = int(input("Digite o numero de testes: "))
nums = []

for i in range(n_testes):
    num = int(input("Digite a possivel senha: "))
    nums.append(num)
    num = num - 1
    print(num)