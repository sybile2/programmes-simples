#permet de trouver le nombre de bits egaux a 1
n = input ("Choisis un entier:")
n = int(n)

i=0
while (n!=0):
    i += (n&1)
    n = n >> 1

print ("Il y a ", i, "bits a 1 pour le nombre ",n,"code en binaire")
