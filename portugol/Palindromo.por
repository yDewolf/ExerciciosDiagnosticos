programa {
  inclua biblioteca Texto
  funcao logico check_palindromo(cadeia palavra) {
    cadeia palindromo
    para (inteiro i = 0; i < Texto.numero_caracteres(palavra); i++) {
      inteiro idx = Texto.numero_caracteres(palavra) - i
      palindromo += palavra[idx - 1]
    }

    retorne palindromo == palavra
  }

  funcao inicio() {
    cadeia palavra
    escreva("Digite uma palavra para descobrir se é um palíndromo: ")
    leia(palavra)
    
    escreva("A palavra ", palavra, " é palindromo? ", check_palindromo(palavra))
  }
}
