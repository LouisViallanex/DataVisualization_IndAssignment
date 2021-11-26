import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from datetime import datetime as dt

plt.rc('axes',edgecolor='w')



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
print("% Hommes: ", 100*conducteurs['1']/sum(conducteurs.values()), " - % Femmes: ", 100*conducteurs['2']/sum(conducteurs.values()))

figFM, axFM = plt.subplots()
axFM.pie([100*conducteurs['1']/sum(conducteurs.values()), 100*conducteurs['2']/sum(conducteurs.values())], colors=['#0984e3','#ff7675'], labels=['♂','♀'], wedgeprops = { 'linewidth' : 7, 'edgecolor' : '#383838' }, textprops={'color':"w"})

# Create a circle at the center of the plot
my_circle = plt.Circle( (0,0), 0.7, color='#383838')
p = plt.gcf()
p.gca().add_artist(my_circle)
axFM.set_title('Proportion of drivers by gender (2020)', color='white')
figFM.patch.set_facecolor('#383838')
       

plt.show()

print("% pers mortes : ", 100 * sum(usagers['grav'] == 2) / len(usagers)) # Pourcentage des personnes impliquées dans un accident qui sont mortes

usagers_decede = usagers.copy()

usagers_decede = usagers_decede.drop(usagers_decede[usagers_decede.grav != 2].index)

#print(usagers_decede)

#print(100 * sum(usagers['grav'] == 2) / len(usagers)) # Pourcentage des personnes impliquées dans un accident qui sont mortes

#print(len(usagers['Num_Acc'].unique())) # Nombre d'accidents

print("% Accidents mortels : ", 100 * len(usagers_decede['Num_Acc'].unique()) / len(usagers['Num_Acc'].unique()) ) # Nbr d'accidents avec mort / Nbr d'accident total = Pourcentage d'accidents mortels

# Il y plus de gens impliqués dans les accidents non mortels. Par exemple 3 voitures (1 personne) et 1 bus (10 pers), si une voiture à un accident mortel on obtient 25% des accidents mortel et 1/14 des personnes impliquées dans un accidents sont mortes.


####################################################################
####################### Repartition par age ########################
####################################################################


#print(usagers)

ageAccidenté = dict.fromkeys(range(130), 0)         # Total accidentés par age
ageMort = dict.fromkeys(range(130), 0)              # Total morts par age
ageAccidenté_prct = dict.fromkeys(range(130), 0)    # % accidentés par age
ageMort_prct = dict.fromkeys(range(130), 0)         # % morts par age

#print(ageAccidenté)

#print(sum(usagers['an_nais']<1921))

for index, row in usagers.iterrows():
    ageAccidenté[2021-row['an_nais']] += 1                                      # Total accidentés par age
    
for index, row in usagers_decede.iterrows():
    ageMort[2021-row['an_nais']] += 1                                           # Total morts par age

for i in ageAccidenté.keys():
    ageAccidenté_prct[i] = ageAccidenté[i] / sum(ageAccidenté.values())         # % accidentés par age
for i in ageMort.keys():
    ageMort_prct[i] = ageMort[i] / sum(ageMort.values())                        # % morts par age

#ageAccidenté_prct = ageAccidenté/sum(ageAccidenté)
#ageMort_prct = ageMort/sum(ageMort)

#print(ageAccidenté)

#fig, axs = plt.subplots(ncols=2)
#ax.bar(ageAccidenté.keys(), ageAccidenté.values())
#plt.show()

#ax.bar(ageMort.keys(), ageMort.values())
"""
axs[0].bar(ageAccidenté.keys(),    ageAccidenté.values(),  color='orange')
axs[0].bar(ageMort.keys(),         ageMort.values(),       color='red')

axs[1].bar(ageAccidenté_prct.keys(),    ageAccidenté_prct.values(),  color='orange')
axs[1].bar(ageMort_prct.keys(),         ageMort_prct.values(),       color='red')

plt.show()
"""

fig3, ax3 = plt.subplots()
ax3.bar(ageAccidenté.keys(),    ageAccidenté.values(),  color='#d63031')
ax3.set_xlim(-5, 105)
ax3.set_title("Age distribution of accident victims (2020)", color="white")
ax3.set_xlabel('Age')
ax3.set_ylabel('Numbers of accidents')
ax3.set_facecolor('#383838')
fig3.patch.set_facecolor('#383838')
ax3.xaxis.label.set_color('w')   
ax3.yaxis.label.set_color('w')         
ax3.tick_params(axis='x', colors='w')   
ax3.tick_params(axis='y', colors='w')

"""
fig4, ax4 = plt.subplots()
ax4.bar(ageMort.keys(),         ageMort.values(),       color='red')
"""

plt.show()

####################################################################
################ Repartition mois, jour, heure, etc ################
####################################################################


caracteristiques = pd.read_csv('caracteristiques-2020.csv', sep=';')

#print(caracteristiques)

repartitionM = dict.fromkeys(range(1, 13), 0)           # Total accidentés par mois
repartitionJ = dict.fromkeys(range(1, 32), 0)            # Total accidentés par jour
repartitionH = dict.fromkeys(range(24), 0)              # Total accidentés par heure

#print(repartitionM)

for index, row in caracteristiques.iterrows():
    repartitionM[row['mois']] += 1                      # Total accidentés par mois

for index, row in caracteristiques.iterrows():
    repartitionJ[row['jour']] += 1                      # Total accidentés par jour

for index, row in caracteristiques.iterrows():
    repartitionH[int(row['hrmn'][:2])] += 1             # Total accidentés par heure

#print(repartitionM)

fig2, axs2 = plt.subplots(ncols=2)
axs2[0].bar(repartitionM.keys(),    repartitionM.values(),  color='#d63031')
#axs2[1].bar(repartitionJ.keys(),    repartitionJ.values(),  color='orange')
axs2[1].bar(repartitionH.keys(),    repartitionH.values(),  color='#d63031')


axs2[0].set_title("Monthly distribution of accidents (2020)", color="white")
axs2[1].set_title("Hourly distribution of accidents (2020)", color="white")

axs2[0].set_xlabel('Month')
axs2[0].set_ylabel('Number of accidents')

axs2[1].set_xlabel('Hour')
axs2[1].set_ylabel('Number of accidents')

axs2[1].set_facecolor('#383838')
fig2.patch.set_facecolor('#383838')
axs2[1].xaxis.label.set_color('w')   
axs2[1].yaxis.label.set_color('w')         
axs2[1].tick_params(axis='x', colors='w')   
axs2[1].tick_params(axis='y', colors='w')
axs2[1].set_xticks(np.arange(0, 24, 2))

axs2[0].set_facecolor('#383838')
axs2[0].xaxis.label.set_color('w')   
axs2[0].yaxis.label.set_color('w')         
axs2[0].tick_params(axis='x', colors='w')   
axs2[0].tick_params(axis='y', colors='w')
axs2[0].set_xticks(np.arange(0, 13, 1))

plt.show()



####################################################################
##################### Repartition geographique #####################
####################################################################


#print(caracteristiques)

import plotly.express as px 

#figMap = px.scatter_geo(caracteristiques, lat = 'lat', lon = 'long', scope = 'europe', opacity=0.1, center = {'lat':46.868376, 'lon':2.725796}, projection='eckert4')
#print(figMap)
#figMap.update_traces(marker=dict(size=5))
#figMap.show()

figMap2 = px.scatter_mapbox(caracteristiques, lat="lat", lon="long", opacity=0.15,
                        color_discrete_sequence=["red"], zoom=4)
figMap2.update_layout(mapbox_style="open-street-map")
figMap2.update_traces(marker=dict(size=4))
figMap2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
figMap2.show()


#caracteristiques_AccMortel = caracteristiques.copy()


#for index, row in caracteristiques_AccMortel.iterrows():
#    if row['Num_Acc'] not in usagers_decede['Num_Acc'].unique():
#       caracteristiques_AccMortel.drop(index, inplace=True)



#print(caracteristiques_AccMortel)


#figMap3 = px.scatter_mapbox(caracteristiques_AccMortel, lat="lat", lon="long", opacity=0.15,
#                        color_discrete_sequence=["red"], zoom=3)
#figMap3.update_layout(mapbox_style="open-street-map")
#figMap3.update_traces(marker=dict(size=4))
#figMap3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#figMap3.show()

# figMap3 représente la carte avec les accidents mortels cette fois ci, mais pas de différence flagrante quant à la répartion de ceux ci.