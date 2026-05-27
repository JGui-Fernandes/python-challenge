import time

from monitor import Monitor

def eh_primo(numero):

    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):

        if numero % i == 0:
            return False

    return True


def geracao_numeros_primos():

    processo = Monitor.gera_pid()

    Monitor.imprime_dados("ANTES", processo)

    inicio = time.time()

    primos = []

    for numero in range(2, 500000):

        if eh_primo(numero):
            primos.append(numero)

    fim = time.time()

    Monitor.imprime_dados("DEPOIS", processo)

    print(f"\nQuantidade de primos: {len(primos)}")

    print(f"Tempo de execução: {fim - inicio:.2f} segundos")

geracao_numeros_primos()