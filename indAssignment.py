import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from datetime import datetime as dt


usagers = pd.read_csv('usagers-2020.csv', sep=';')

#print(usagers)

conducteurs = {'1':0, '2':0}

for index, row in usagers.iterrows():
    if row['catu'] == 1: # Catu 1 = conducteur
            if row['sexe'] == 1:
                conducteurs['1'] += 1
            elif row['sexe'] == 2:
                conducteurs['2'] += 1

# Pourcentage des conducteurs impliqués dans un accident
print("Hommes: ", 100*conducteurs['1']/sum(conducteurs.values()), " - Femmes: ", 100*conducteurs['2']/sum(conducteurs.values()))


print(100 * sum(usagers['grav'] == 2) / len(usagers)) # Pourcentage des personnes impliquées dans un accident qui sont mortes

usagers_decede = usagers.copy()

usagers_decede = usagers_decede.drop(usagers_decede[usagers_decede.grav != 2].index)

#print(usagers_decede)

#print(100 * sum(usagers['grav'] == 2) / len(usagers)) # Pourcentage des personnes impliquées dans un accident qui sont mortes

print(len(usagers['Num_Acc'].unique())) # Nombre d'accidents

print(100 * len(usagers_decede['Num_Acc'].unique()) / len(usagers['Num_Acc'].unique()) ) # Nbr d'accidents avec mort / Nbr d'accident total = Pourcentage d'accidents mortels

# Il y plus de gens impliqués dans les accidents non mortels. Par exemple 3 voitures (1 personne) et 1 bus (10 pers), si une voiture à un accident mortel on obtient 25% des accidents mortel et 1/14 des personnes impliquées dans un accidents sont mortes.

# Repartition par age 

#print(usagers)

ageAccidenté = dict.fromkeys(range(130), 0)
ageMort = dict.fromkeys(range(130), 0)
ageAccidenté_prct = dict.fromkeys(range(130), 0)
ageMort_prct = dict.fromkeys(range(130), 0)

#print(ageAccidenté)

#print(sum(usagers['an_nais']<1921))

for index, row in usagers.iterrows():
    ageAccidenté[2021-row['an_nais']] += 1
    
for index, row in usagers_decede.iterrows():
    ageMort[2021-row['an_nais']] += 1

for i in ageAccidenté.keys():
    ageAccidenté_prct[i] = ageAccidenté[i] / sum(ageAccidenté.values())
for i in ageMort.keys():
    ageMort_prct[i] = ageMort[i] / sum(ageMort.values())

#ageAccidenté_prct = ageAccidenté/sum(ageAccidenté)
#ageMort_prct = ageMort/sum(ageMort)

#print(ageAccidenté)

fig, axs = plt.subplots(ncols=2)
#ax.bar(ageAccidenté.keys(), ageAccidenté.values())
#plt.show()

#ax.bar(ageMort.keys(), ageMort.values())

axs[0].bar(ageAccidenté.keys(),    ageAccidenté.values(),  color='orange')
axs[0].bar(ageMort.keys(),         ageMort.values(),       color='red')

axs[1].bar(ageAccidenté_prct.keys(),    ageAccidenté_prct.values(),  color='orange')
axs[1].bar(ageMort_prct.keys(),         ageMort_prct.values(),       color='red')


plt.show()