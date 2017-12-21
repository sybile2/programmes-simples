#tri par selection
t = [17, 2, 14, 42, 8, 1, 12, 6, 4 ,16]
print(sorted(t))

n = len(t)
for i in range(n):
    posmini = i
    for j in range(i+1,n):
        if t[j] < t[posmini]:
           posmini = j
    (t[i],t[posmini]) = (t[posmini],t[i])
print(t)
