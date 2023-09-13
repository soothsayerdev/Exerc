# Resolucao pelo GPT

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def calculate_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                factors.append(n)
            break
    return factors

def game_winner(A, B):
    if A == B:
        return '?'
    max_num = max(A, B)
    min_num = min(A, B)
    factors = set()
    
    for num in range(min_num + 1, max_num):
        factors.update(calculate_factors(num))
        if len(factors) >= max_num - min_num - 1:
            break
    
    if len(factors) >= max_num - min_num - 1:
        return 'Bob'
    else:
        return 'Alice'

# Leitura dos números escolhidos por Alice e Bob
A, B = map(int, input().split())

# Determinação do vencedor do jogo
winner = game_winner(A, B)

# Impressão do resultado
print(winner)
