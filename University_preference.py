import pandas as pd

Datasheet = pd.read_excel('Faculty Database.xlsx', skiprows = 1)
input_University = input("Enter a University")
DS = Datasheet.loc[(Datasheet['University/Institute'] == input_University)]
DS = DS.append(Datasheet.loc[(Datasheet['University/Institute'] != input_University)])
DS.to_excel('Faculty Database.xlsx', sheet_name='Faculty Database')
