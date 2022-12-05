import re
#This function takes a string as input and gives numeric score as an output
def PHD(string):
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