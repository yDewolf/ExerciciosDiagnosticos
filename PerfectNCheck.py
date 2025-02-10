def check_perfect(n):
    total: int = 0
    for prev in range(n):
        if prev == n or prev == 0:
            continue
    
        if n % prev == 0: # N é divisível por
            total += prev
            if total > n:
                return False

    return total == n

max_number = int(input("Digite a quantidade de números a serem checados: "))

for n in range(max_number + 1):
    if check_perfect(n):
        print(f"O número {n} é perfeito")
        continue
