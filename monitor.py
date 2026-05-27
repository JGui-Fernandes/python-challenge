import psutil
import os


class Monitor:

    @staticmethod
    def imprime_dados(etapa, pid=None):
        print(f"\n{etapa}")

        print('Núcleos:', os.cpu_count())

        cpu = psutil.cpu_percent(interval=1)
        print('CPU:', cpu, '%')

        memoria_sistema = psutil.virtual_memory()
        print('Memória do sistema:', memoria_sistema.percent, '%')

        if pid is not None:
            memoria_processo = pid.memory_info().rss / 1024 / 1024
            print(f'Memória do processo: {memoria_processo:.2f} MB')

    @staticmethod
    def gera_pid():
        return psutil.Process(os.getpid())