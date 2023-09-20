num = int(input("Digite um numero para descobrir o fatorial: "))
fat = 1
c = 1

#while(c <= num):
    #fat = fat * c
    #c += 1
    #print(fat)
# FATORAIAL D UM NUMERO
for i in range(1, num + 1):
    fat = fat * i
    print(fat)
