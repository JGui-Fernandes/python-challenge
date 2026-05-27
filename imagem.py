import time
from PIL import Image, ImageFilter
import numpy as np
import uuid

from monitor import Monitor

def processamento_imagens():

    processo = Monitor.gera_pid()

    Monitor.imprime_dados("ANTES", processo)

    inicio = time.time()

    largura = 4000
    altura = 4000

    array = np.random.randint(0, 255, (altura, largura, 3), dtype=np.uint8)

    imagem = Image.fromarray(array)

    imagem = imagem.filter(ImageFilter.GaussianBlur(radius=10))

    imagem.save(f"image_{uuid.uuid4()}.png")

    fim = time.time()

    Monitor.imprime_dados("DEPOIS", processo)

    print(f"\nTempo de execução: {fim - inicio:.2f} segundos")

processamento_imagens()
