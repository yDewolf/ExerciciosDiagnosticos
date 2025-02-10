def check_prime(n):
    for prev in range(n):
        if prev == n or prev <= 1:
            continue
    
        if n % prev == 0: # N é divisível por
            return False

    return True

max_number = int(input("Digite a quantidade de números a serem checados: "))

for n in range(max_number + 1):
    if check_prime(n):
        print(f"O número {n} é primo")
        continue
