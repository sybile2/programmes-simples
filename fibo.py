#calcule le nieme terme de la suite de fibonacci
a = 0
b = 1
t = 2
n = 20


if n == 0:
    print("le",n,"ieme terme de la suite de fibo est ",a)

elif n == 1:
    print("le",n,"ieme terme de la suite de fibo est ",b)

else:
    while t <= n:
        z = a
        a = b
        b = z + b
        t += 1
    print("le",n,"ieme terme de la suite de fibo est ",b)


