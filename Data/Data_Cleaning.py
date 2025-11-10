"""
Apples to Apples
Data Cleaning
"""

#imports
import pandas as pd 

apples_flavor = pd.read_csv('Data/apple_flavor.csv')


apple_names = pd.read_csv('Data/Rittman_Orchard.csv')
print(apples_flavor.columns)
print(apple_names.columns)

apple_names = apple_names[['Variety', 'Description']]

apples_flavor = apples_flavor[['Size', 'Sweetness', 'Crunchiness', 'Juiciness', 'Ripeness', 'Acidity']]

apple_names.to_csv('Apples_Names.csv', index= False)
apples_flavor.to_csv('Apple_Flavors', index= False)