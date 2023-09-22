a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
d = int(input("Digite o valor de D: "))

if b > c:
    if a % 2 == 0:    
        if c and d < 0:
            if d > a:
                if (a + b) < (c + d):
                    print("Valores aceitos")
                else:
                    print("Valores nao aceitos")