#somme des n premiers nombres
n = '89'
s = 0

try :
    t = int(n)
    if t>0:
        for i in range(1,t+1):
            s = s+i
        print(s)
    else:
        print("ceci n'est pas un entier positif non nul")
except:
    print("ceci n'est pas un entier")

