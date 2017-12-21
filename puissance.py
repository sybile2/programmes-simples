#calcule un nombre a la puissance n
import time

a = 2
n = 200000
i = 1
res = a


tmps1=time.clock()

while i != n:
    res = a*res
    i += 1
print("la",n,"ieme puissance de ",a, "est",res)

tmps2=time.clock()

print ("vitesse d'execution de cette premiere methode: ",tmps2 - tmps1)
