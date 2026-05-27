import time
import uuid

from monitor import Monitor


def processamento_arquivos():

    processo = Monitor.gera_pid()

    Monitor.imprime_dados("ANTES", processo)

    inicio = time.time()

    nome_arquivo = f"{uuid.uuid4()}.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:

        for i in range(5_000_000):
            arquivo.write(f"Linha número {i}\n")

    contador = 0

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        for linha in arquivo:
            contador += 1

    fim = time.time()

    Monitor.imprime_dados("DEPOIS", processo)

    print(f"\nArquivo gerado: {nome_arquivo}")

    print(f"Total de linhas: {contador}")

    print(f"Tempo de execução: {fim - inicio:.2f} segundos")


processamento_arquivos()