
import pandas as pd
 
 df = pd.read_excel('Faculty_Database.xlsx' , skiprows = 1)
 df.sort_values(by=['Year of Completion '], ascending=True)







