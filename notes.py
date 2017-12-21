#retourne une note
n = 321

if 0<=n<11:
        note = 'E'
elif 11<=n<21:
        note = 'D'
elif 21<=n<31:
        note = 'C'
elif 31<=n<41:
        note = 'B'
elif 41<=n<51:
        note = 'A'
else:
    note = "ceci n'est pas possible"

print("Note de l'eleve:",note)

