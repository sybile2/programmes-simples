#calcule un salaire
n = 45
sh = 10
salaire = 0

if n <=35:
        salaire = n * sh
else:
        salaire = sh * (35 + 1.5*(n-35))

print ("le salaire total sera de: ", salaire)
