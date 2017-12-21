#calcule un nombre a la puissance n
import time

a = 2
n = 200000
i = 1
res = a

tmps3=time.clock()

if n % 2 == 0:
    while i != n/2:
        res = a*res
        i += 1
    res = res*res
    print("la",n,"ieme puissance de ",a, "est",res)
else:
    while i != (n-1)/2:
        res = a*res
        i += 1
    res = res*res*a
    print("la",n,"ieme puissance de ",a, "est",res)

tmps4=time.clock()

print ("vitesse d'execution de cette deuxieme methode: ",tmps4 - tmps3)
