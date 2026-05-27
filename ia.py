import time
import numpy as np

from monitor import Monitor

def simulacao_ia():

    processo = Monitor.gera_pid()

    Monitor.imprime_dados("ANTES", processo)

    inicio = time.time()

    matriz1 = np.random.rand(3000, 3000)
    matriz2 = np.random.rand(3000, 3000)

    resultado = np.dot(matriz1, matriz2)

    fim = time.time()

    Monitor.imprime_dados("DEPOIS", processo)

    print(f"\nResultado gerado: {resultado.shape}")

    print(f"Tempo de execução: {fim - inicio:.2f} segundos")

simulacao_ia()