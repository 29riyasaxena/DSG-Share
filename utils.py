import re
import pandas as pd
import numpy as np

#This function takes a string as input and gives numeric score as an output
def PHD_score(string):
  if string == None:
    return 0
# Giving a score of 0 to missing values
# Split the function about comma if it exists
  x = re.split(',',string) 
  y = 0
  z = 0
  for t in x:
    temp = re.findall(r'\d+', t)
    res = list(map(int, temp))
    if "Supervision" in t:
      y = res[0]
    else:
      z = res[0]
# 0.5 score to under supervision and 1 to completed
  return 0.5*y + z

def dept(x):
  d = {
      "APD" : "Department of Architecture and Planning",
       "AMSC" : "Department of Applied Mathematics and Scientific Computing",
        "BSBE" : "Department of Biosciences and Bioengineering",
        "CED" : "Department of Civil Engineering",
        "CHED" : "Department of Chemical Engineering",
        "CSE" : "Department of Computer Science and Engineering",
        "CYD" : "Department of Chemistry",
        "ECD" : "Department of Electronics and Communication Engineering",
        "EED" : "Department of Electrical Engineering",
        "EQD" : "Department of Earthquake Engineering",
        "ESD" : "Department of Earth Sciences",
        "HRED" : "Department of Hydro and Renewable Energy",
        "HSSD" : "Department of Humanities and Social Sciences",
        "HYD" : "Department of Hydrology",
        "MTD" : "Department of Mathematics",
        "MIED" : "Department of Mechanical and Industrial Engineering",
        "MSD" : "Department of Management Studies",
        "MMED" : "Department of Metallurgical and Materials Engineering",
        "PPE" : "Department of Polymer and Process Engineering",
        "PHY" : "Department of Physics",
        "PT" : "Department of Paper Technology",
        "WRDM" : "Department of Water Resources Development and Management",
        "DES" : "Department of Design"
    }
    return d[x]

def Specializations(string):
  return re.split(",|;",string)

def Designation(df):
  designation_categories = ["Professor Emeritus","Professor Of Practice", "Retired Faculty", "HAG - Professor", "Professor", "Associate Professor", "Assistant Professor"]
  df["Designation"] = pd.Categorical(df["Designation"], categories = designation_categories)
  return df.sort_values(by = "Designation")
  

def YOC(df): return  df.sort_values(by=['Year of Completion '], ascending=True)

def University(string, datasheet):
  DS = Datasheet.loc[(Datasheet['University/Institute'] == input_University)]
  DS = DS.append(Datasheet.loc[(Datasheet['University/Institute'] != input_University)])
  return DS
  

