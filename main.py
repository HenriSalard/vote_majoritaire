import pandas as pd

file = pd.read_csv('comptes.csv',sep = ';')

# Accede aux colonnes individuelles
noms_des_colonnes = file.columns
print(noms_des_colonnes)

# On parcourt le fichier ligne par ligne
for index, row in file.iterrows():
   print("Le",row['date'], " la tresorerie est de ", row['montant'], "€ soit une difference de : ", row['difference'])

# On peut mettre dans une liste
list1 = []
for index, row in file.iterrows():
    list1.append(row['montant'])