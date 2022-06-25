# temp={
#     'Assault','Accident','Fraud','Harrassment','Theft','Buglary','Drugs','Weapon Violence','Shooting','Other'
# }

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
CRIMINAL MISCHIEF & RELATED OF
POSSESSION OF STOLEN PROPERTY
FOR OTHER AUTHORITIES
MOVING INFRACTIONS
ESCAPE 3
NEW YORK CITY HEALTH CODE
"""

temp = {
    'FELONY SEX CRIMES': l['s'],
    'PARKING OFFENSES': l['tf'],
    'LOITERING/GAMBLING (CARDS, DIC': l['p'],
    'HOMICIDE-NEGLIGENT-VEHICLE': l['mu'],
    'JOSTLING': l['p'],
    'SEX CRIMES': l['s'],
    'RAPE': l['s'],
    'ARSON': l['ar'],
    'ASSAULT 3 & RELATED OFFENSES': l['as'],
    'FELONY ASSAULT': l['as'],
    'DANGEROUS WEAPONS': l['g'],
    'PETIT LARCENY': l['r'],
    'GRAND LARCENY OF MOTOR VEHICLE': l['t'],
    'DANGEROUS DRUGS': l['d'],
    'GRAND LARCENY': l['r'],
    'OTHER OFFENSES RELATED TO THEF': l['t'],
    'OFFENSES AGAINST PUBLIC ADMINI': l['p'],
    'ROBBERY': l['r'],
    'OTHER TRAFFIC INFRACTION': l['tf'],
    'FORGERY': l['f'],
    'CRIMINAL MISCHIEF & RELATED OF': l['as'],
    'INTOXICATED & IMPAIRED DRIVING': l['tf'],
    'MURDER & NON-NEGL. MANSLAUGHTE': l['mu'],
    'UNAUTHORIZED USE OF A VEHICLE': l['tf'],
    'BURGLARY': l['r'],
    'OFFENSES INVOLVING FRAUD': l['f'],
    'VEHICLE AND TRAFFIC LAWS': l['tf'],
    'OFF. AGNST PUB ORD SENSBLTY &': l['p'],
    'THEFT OF SERVICES': l['t'],
    'CRIMINAL TRESPASS': l['p'],
    'POSSESSION OF STOLEN PROPERTY': l['t'],
    'HARRASSMENT 2': l['h'],
    'THEFT-FRAUD': l['f'],
    'CHILD ABANDONMENT/NON SUPPORT': l['cc'],
    'ENDAN WELFARE INCOMP': l['p'],
    'OFFENSES AGAINST THE PERSON': l['as'],
    'KIDNAPPING & RELATED OFFENSES': l['mi'],
    'FRAUDULENT ACCOSTING': l['f'],
    'FRAUDS': l['f'],
    'ALCOHOLIC BEVERAGE CONTROL LAW': l['p'],
    'INTOXICATED/IMPAIRED DRIVING': l['tf'],
    'GAMBLING': l['p'],
    'OFFENSES AGAINST PUBLIC SAFETY': l['p'],
    'KIDNAPPING': l['mi'],
    'ANTICIPATORY OFFENSES': l['p'],
    'HOMICIDE-NEGLIGENT,UNCLASSIFIE': l['mu'],
    'DISORDERLY CONDUCT': l['p'],
    'FRAUDULENT ACCOSTING': l['f'],
    'OFFENSES RELATED TO CHILDREN': l['cc'],
}
with open("map.json", "w") as outfile:
    json.dump(temp,outfile)


