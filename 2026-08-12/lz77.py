from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import komm

with open("alice.txt", "rb") as f:
    entrada = list(f.read())

lz77 = komm.LempelZiv77Code(
    search_size=2**12,
    lookahead_size=32,
    source_cardinality=256,
)

# compressão
codificado = lz77.encode(entrada)
size = len(codificado)
# pad para multiplo de 8
codificado = np.pad(codificado, (0,8 - size % 8))

with open("alice.lz77", "wb") as f:
    bytes = komm.bits_to_int(codificado.reshape(-1, 8))
    bytes = bytes.astype(np.uint8)
    f.write(bytes)

print(f"Tamanho original: {len(entrada)}")
print(f"Tamanho comprimido: {len(codificado)/8}")

# descompressão

with open("alice.lz77", "rb") as f:
    bytes = list(f.read())

bits = komm.int_to_bits(bytes, width=8).reshape(-1)
bits = bits[:size]                                      # remove o pad
saida = lz77.decode(bits)
print(saida)

with open("alice2.txt", "wb") as f:
    bytes = saida.astype(np.uint8)
    f.write(bytes)