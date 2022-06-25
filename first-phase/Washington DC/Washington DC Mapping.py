import json


l = {
    'as': 'Assault',
    'ac': 'Accident',
    'tf': 'Traffic Law',
    'ht': 'Human Trafficking',
    'ar': 'Arson',
    'd': 'Drugs',
    'mi': 'Missing',
    'mu': 'Murder',
    'p': 'Public Nuisance',
    't': 'Theft',
    'r': 'Robbery',
    'g': 'Gun Violence',
    's': 'Sex Crime',
    'f': 'Fraud',
    'o': 'Others',
    'h': 'Harrassment',
    'cc': 'Child Crime',
}

"""
Release Violations/Fugitive
Other Crimes
Liquor Law Violations
"""

temp = {
    'Theft from Auto': l['t'],
    'Motor Vehicle Theft': l['r'],
    'Homicide':l['mu'],
    'Aggravated Assault':l['as'],
    'Simple Assault': l['as'],
    'Traffic Violations': l['tf'],
    'Narcotics': l['d'],
    'Weapon Violations': l['g'],
    'Driving/Boating While Intoxicated': l['ac'],
    'Damage to Property': l['p'],
    'Offenses Against Family & Children': l['cc'],
    'Assault with a Dangerous Weapon': l['as'],
    'Theft': l['t'],
    'Property Crimes': l['f'],
    'Assault on a Police Officer': l['as'],
    'Prostitution': l['ht'],
    'Disorderly Conduct': l['p'],
    'Robbery': l['r'],
    'Burglary': l['r'],
    'Sex Offenses': l['s'],
    'Fraud and Financial Crimes': l['f'],
    'Sex Abuse': l['s'],
    'Arson': l['ar'],
    'Kidnapping': l['mi'],
    'Gambling': l['p'],
}

with open("map.json", "w") as outfile:
    json.dump(temp,outfile)