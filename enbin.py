# donne un nombre en binaire
import math

n = 1024
i = 0
k = math.floor(math.log(n) / math.log(2))
tab = []

while n != 0:
    tab.append((n & 1))
    n = n >> 1
    i += 1

for j in range(0, k + 1):
    print(tab[k - j], end='\t')
