def check_palindromo(word: str):
    reversed_word = ""
    for i in range(len(word)):
        idx: int = (len(word) - i) # Reverse idx
        reversed_word += word[idx - 1]
    
    return reversed_word == word

word = input("Digite uma palavra (Sem espaços): ")
print(check_palindromo(word))
