import time

from monitor import Monitor

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

def calculo_matematico_pesado():

    processo = Monitor.gera_pid()

    Monitor.imprime_dados("ANTES", processo)

    inicio = time.time()

    resultado = fibonacci(42)

    fim = time.time()

    Monitor.imprime_dados("DEPOIS", processo)

    print(f"\nResultado: {resultado}")

    print(f"Tempo de execução: {fim - inicio:.2f} segundos")


calculo_matematico_pesado()