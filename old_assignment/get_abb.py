"""
Functie die de gegeven naam omzetten naar de afkorting van het treinstation.
De afkortingen zijn verkregen via:
https://wiki.ovinnederland.nl/wiki/Lijst_van_verkortingen_van_treinstations 
"""

import pandas as pd

def verkorting_station(naam):
    afk = pd.read_excel("spoorwegafkortingen.xlsx", names = ['Afkorting', 'FE-code', 'Naam', 'Opmerking'], header=None)
    afk = afk.drop(columns=['FE-code', 'Opmerking'])
    afk['Naam'] = afk['Naam'].str.lower()
    try:
        afkorting = afk.loc[afk['Naam'] == naam.lower()]['Afkorting'].values[0]
    except:
        afkorting = 0
    
    # check if the abbrevation is valid, if not try other name, other return 0
    if afkorting == 0:
        original = naam
        naam = original + ' centraal'
        try:
            afkorting = afk.loc[afk['Naam'] == naam.lower()]['Afkorting'].values[0]
        except:
            afkorting = 0

    if afkorting == 0:
        naam = original + ' centrum'
        try:
            afkorting = afk.loc[afk['Naam'] == naam.lower()]['Afkorting'].values[0]
        except:
            afkorting = 0
    
    if afkorting == 0:
        return 0
    
    afkorting = afkorting.rstrip()

    return afkorting