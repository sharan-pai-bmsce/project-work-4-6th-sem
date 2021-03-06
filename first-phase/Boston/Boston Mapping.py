import json


l={ 'as':'Assault',
    'ac':'Accident',
    'ar':'Arson',
    'f':'Fraud',
    'd':'Drugs',
    'mi':'Missing',
    'mu':'Murder',
    'p':'Public Nuisance',
    't':'Theft',
    'r':'Robbery',
    'g':'Gun Violence',
    's':'Sex Crime',
    'o':'Others'
}

temp={
    'BURGLARY - RESIDENTIAL': l['r'],
    'INVESTIGATE PROPERTY':l['o'],
    'PROPERTY - LOST/ MISSING':l['mi'],
    'M/V ACCIDENT - OTHER':l['ac'],
    'LARCENY THEFT FROM BUILDING':l['t'],
    'FRAUD - CREDIT CARD / ATM FRAUD':l['f'],
    'FRAUD - FALSE PRETENSE / SCHEME':l['f'],
    'VANDALISM':l['p'],
    'FRAUD - WIRE':l['f'],
    'LARCENY SHOPLIFTING':l['r'],
    'AUTO THEFT':l['t'],
    'LARCENY THEFT OF BICYCLE':l['t'],
    'LARCENY THEFT FROM MV - NON-ACCESSORY':l['t'],
    'HARASSMENT/ CRIMINAL HARASSMENT':l['as'],
    'LARCENY THEFT OF MV PARTS & ACCESSORIES':l['t'],
    'M/V - LEAVING SCENE - PROPERTY DAMAGE':l['p'],
    'PROPERTY - LOST THEN LOCATED':l['mi'],
    'THREATS TO DO BODILY HARM':l['as'],
    'BURGLARY - COMMERICAL':l['r'],
    'M/V ACCIDENT - PROPERTY DAMAGE':l['ac'],
    'ASSAULT - SIMPLE':l['as'],
    'AUTO THEFT - MOTORCYCLE / SCOOTER':l['t'],
    'STOLEN PROPERTY - BUYING / RECEIVING / POSSESSING':l['f'],
    'ASSAULT - AGGRAVATED':l['as'],
    'FIRE REPORT':l['ar'],
    'LARCENY ALL OTHERS':l['t'],
    'ROBBERY':l['r'],
    'M/V ACCIDENT - INVOLVING BICYCLE - INJURY':l['ac'],
    'MISSING PERSON - LOCATED':l['mi'],
    'FRAUD - IMPERSONATION':l['f'],
    'M/V ACCIDENT - INVOLVING PEDESTRIAN - NO INJURY':l['ac'],
    'LARCENY PICK-POCKET':l['t'],
    'SUDDEN DEATH':l['mu'],
    'M/V ACCIDENT - PERSONAL INJURY':l['ac'],
    'EVADING FARE':l['f'],
    'THREATS TO DO BODILY HARM':l['as'],
    'PROPERTY - LOST/ MISSING':l['t'],
    'DRUGS - POSSESSION/ SALE/ MANUFACTURING/ USE':l['d'],
    'FRAUD - FALSE PRETENSE / SCHEME':l['f'],
    'Justifiable Homicide':l['mu'],
    'MANSLAUGHTER - NEGLIGENCE':l['mu'],
    'KIDNAPPING/CUSTODIAL KIDNAPPING/ ABDUCTION':l['mi'],
    'EXPLOSIVES - TURNED IN OR FOUND':l['g'],
    'PROSTITUTION - SOLICITING':l['s'],
    'ARSON':l['ar'],
    'MURDER, NON-NEGLIGIENT MANSLAUGHTER':l['mu'],
    'GRAFFITI':l['p'],
    'NOISY PARTY/RADIO-NO ARREST':l['p'],
    'DRUNKENNESS':l['p']
}
with open("map.json", "w") as outfile:
    json.dump(temp,outfile)