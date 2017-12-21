# trie par insertion

t = [5,54,78,6,246,43]

for i in range (1, len(t)):
    a = t[i]
    j = i
    while ((t[j] < t[j-1]) & (j > 0)):
        t[j] = t[j-1]
        j = j-1
        t[j] = a


print (t)
