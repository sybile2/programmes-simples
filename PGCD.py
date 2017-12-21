#calcule le pgcd de deux nombres entiers
n = 490
m = 490
r = 12
pgcd = 1

if m == n:
    pgcd = n
    print ("Le PGCD est : ",pgcd)
else :
    if m > n :
        t = n
        n = m
        m = t
    while r != 0:
        r = n % m
        if r != 0:
            n = m
            m = r
        if r == 0:
            pgcd = m
            print ("Le PGCD est : ",pgcd)


