num1 = int(input("Digite seu primeiro numero: "))
num2 = int(input("Digite seu segundo numero: "))
j = 0

for i in range(num1,num2 + 1):
    if (i % 13 != 0):
        j += i
print(j)
        
        
    
    

    