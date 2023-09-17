num = int(input("Digite um numero para descobrir seus divisores: "))

for i in range(1,num +1):
    if num % i == 0:
        print(i)


