import os

maman_an = input ("Quelle est la date de naissance de ta maman (année)?")
m_an = int (maman_an)

maman_mois = input ("Quelle est la date de naissance de ta maman (mois)?")
m_mois = int (maman_mois)

maman_jour = input ("Quelle est la date de naissance de ta maman (jour)?")
m_jour = int (maman_jour)

toi_an = input ("Quelle est ta date de naissance (année)?")
t_an = int (toi_an)

toi_mois = input ("Quelle est ta date de naissance (mois)?")
t_mois = int (toi_mois)

toi_jour = input ("Quelle est ta date de naissance (jour)?")
t_jour = int (toi_jour)


d_an = 0
d_mois = 0
d_jour = 0
if t_mois - 1 == 2 :
    if t_an % 400 == 0 or (t_an % 4 == 0 and t_an % 100 != 0):
        nb_jour_mois = 29
    else:
        nb_jour_mois = 28
elif t_mois - 1 == 1 or 3 or 5 or 7 or 8 or 10 or 12 :
    nb_jour_mois = 31
else:
    nb_jour_mois = 30

if m_mois <= t_mois:
    d_an = t_an - m_an
else :
    d_an = t_an - m_an - 1

if m_mois <= t_mois and m_jour <= t_jour:
    d_mois = t_mois - m_mois
elif m_mois <= t_mois and m_jour >= t_jour:
    d_mois = t_mois - m_mois - 1
elif m_mois >= t_mois and m_jour <= t_jour:
    d_mois = 12 - m_mois + t_mois
else:
    d_mois = 12 - m_mois + t_mois - 1


if m_jour <= t_jour:
    d_jour = t_jour - m_jour
else:
    d_jour = nb_jour_mois - m_jour + t_jour


print ("Ta maman a accouché à: ",d_an," ans, ",d_mois," mois et ",d_jour," jours")

os.system("pause")
