programa {
  funcao logico check_perfect(inteiro n) {
    inteiro total
    total = 0
    para (inteiro prev = 1; prev < n; prev++) {
      se (n % prev == 0) {
        total += prev
        se (total > n) {
          retorne falso
        }
      }
    }

    retorne total == n
  }

  funcao inicio() {
    inteiro maximo
    escreva("Informe o valor máximo a ser buscado sla: ")
    leia(maximo)

    para (inteiro n = 0; n <= maximo; n++) {
      se (check_perfect(n)) {
        escreva("O número ", n, " é perfeito\n")
      }
    }
  }

}
