import random
import time

from monitor import Monitor


def ordenar_vetor():
    processo = Monitor.gera_pid()

    Monitor.imprime_dados("ANTES", processo)

    inicio = time.time()

    vetor = [random.randint(0, 100000000) for _ in range(10_000_000)]

    vetor.sort()

    fim = time.time()

    Monitor.imprime_dados("DEPOIS", processo)

    print(f"\nTempo de execução: {fim - inicio:.2f} segundos")

ordenar_vetor()
