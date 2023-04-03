# DSG-Share
A repository for the collab project of DSG and ShARE

# Deep into the code
We used re library, a regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check if a particular string matches a given regular expression. Here we used it for matching with comma.


Dept(string) This function is used to convert department names which are in short form to long form for better understanding.

Specializations(string) This function is used in splits the words(specialisation) for deeper research.

Designation(df) This function has sorted the designation of all professors in an Descending order accordingly

   1."Professor Emeritus"
   2."Professor Of Practice"
   3."Retired Faculty"
   4."HAG - Professor"
   5."Professor"
   6."Associate Professor"
   7."Assistant Professor"
   
 Professor Emeritus > Professor Of Practice > Retired Faculty > HAG - Professor > Professor > Associate Professor > Assistant Professor
 
PHD_score(string)  gives score of 0.5 to PHD under supervision and 1 to completed.

YOC(df) sorts the PHDs based on year of completion of their PHD in ascending order.

# EDA
Necessary modules were imported and dataframe taking into consideration only first 125 columns were used to infer information.
A pie chart is created to show the department wise division of the faculty for the considered dataframe.
Unique values of designation and departments were taken upto the considered dataframe and then bar graph for each department showing designation distribution of the professor is made
Then each designation is provided by a number based on their order and irrelevant columns like E-Mail and Telephone have been removed.
An inference about the gender base division for the faculty members is made using a pie chart

Then a countplot representing the number of profs who graduated between the specified year categories is made while having a gender-wise comparision.

Combinations of 2-3 columns have been interlinked and their relative counts have been displayed as countplots for visual understanding of the data.

Next, a graphical inference is made to analyze the distribution of faculty members based on the country from which they graduated.



