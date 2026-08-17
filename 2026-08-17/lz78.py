from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import komm

with open("alice.txt", "rb") as f:
    entrada = list(f.read())

lz78 = komm.LempelZivWelchCode(
    source_cardinality=256,
)

# compressão
codificado = lz78.encode(entrada)
size = len(codificado)
# pad para multiplo de 8
codificado = np.pad(codificado, (0,8 - size % 8))

with open("alice.lz78", "wb") as f:
    bytes = komm.bits_to_int(codificado.reshape(-1, 8))
    bytes = bytes.astype(np.uint8)
    f.write(bytes)

print(f"Tamanho original: {len(entrada)}")
print(f"Tamanho comprimido: {len(codificado)/8}")

# descompressão

with open("alice.lz78", "rb") as f:
    bytes = list(f.read())

bits = komm.int_to_bits(bytes, width=8).reshape(-1)
bits = bits[:size]                                      # remove o pad
saida = lz78.decode(bits)
print(saida)

with open("alice2.txt", "wb") as f:
    bytes = saida.astype(np.uint8)
    f.write(bytes)