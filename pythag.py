#ecrit la table de pythagore
n = input ("Give me an integer:")

print ("Voici la table de pythagore correspondante:")
n = int(n)
i = 1
j = 1
k = 1
print("|\t x | ",end = '\t')
while i <= n:
        print (" ",i,"|", end = '\t')
        i+=1
print ('\n')
while j <= n:
        print("|\t", j,"| ",end = '\t')
        while k <= n:
                print (" ",k*j,"|", end = '\t')
                k+=1
        print ('\n')
        k = 1
        j += 1

