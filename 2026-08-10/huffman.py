from collections import Counter
import struct
import numpy as np
import matplotlib.pyplot as plt
import komm

with open("alice.txt", "rb") as f:
    entrada = list(f.read())

c = Counter(entrada)
pmf = [c[i] / len(entrada) for i in range(256)]

# plt.stem(pmf)
# plt.show()
print(f"Entropia: {komm.entropy(pmf):.2f}")

code = komm.HuffmanCode(pmf)
print(f"Taxa dp codigo: {code.rate(pmf):.2f}")

codificado = code.encode(entrada)
# pad para multiplo de 8
codificado = np.concatenate([codificado, [0,0,0]])

with open("alice.huff", "wb") as f:
    bytes = komm.bits_to_int(codificado.reshape(-1, 8))
    bytes = bytes.astype(np.uint8)
    f.write(bytes)

print(f"Tamanho original (bits): {len(entrada)*8}")
print(f"Tamanho comprimido (bits): {len(codificado)}")

