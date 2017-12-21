#permet de trouver le nombre de bits egaux a 1
n = input ("Choisis un entier:")
n = int(n)

k = 1
resultat = 0
reste = n

if n == 0: resultat = 0
elif n == 1: resultat = 1
else:
    while reste > 1:
        while 2*k <= reste:
            k = 2*k
        reste = reste - k
        k = 1
        resultat += 1
    if reste == 1:
        resultat += 1
print ("Il y a ", resultat, "bits a 1 pour le nombre ",n,"code en binaire")
