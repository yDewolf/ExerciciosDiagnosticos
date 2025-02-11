programa {
  funcao logico check_prime(inteiro n) {
    para (inteiro prev = 2; prev < n; prev++) {
      se (n % prev == 0) {
        retorne falso
      }
    }

    retorne verdadeiro
  }

  funcao inicio() {
    inteiro maximo
    escreva("Informe o valor máximo a ser buscado sla: ")
    leia(maximo)

    para (inteiro n = 0; n <= maximo; n++) {
      se (check_prime(n)) {
        escreva("O número ", n, " é primo\n")
      }
    }
  }

}
