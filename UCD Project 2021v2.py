import pandas as pd
import numpy as np
import matplotlib as mat

Crossfit_Athletes_2020 = pd.read_csv('TwentyTwenty_opens_athletes.csv')
Crossfit_Athletes_2020_Scores = pd.read_csv('2020_opens_scores.csv')

print(Crossfit_Athletes_2020.columns)

Crossfit_Athletes_2020.set_index("competitorid")

#Crossfitsort1 = Crossfit_Athletes_2020.sort_index()#

#print(Crossfitsort1)#

Crossfitsorted =Crossfit_Athletes_2020.sort_values("competitorid")

print(Crossfitsorted)

Crossfitduplicates_removed = Crossfitsorted.drop_duplicates(subset='competitorid', keep="first")

print(Crossfitduplicates_removed)



#grouping

#slicing

#iloc#

#Itterows#

# merge data frames#

#Crossfit_Athletes_2020['competitorid'] = Crossfit_Athletes_2020.index#



#print(Crossfit_Athletes_2020['height'])#
#print(Crossfit_Athletes_2020['weight'])#



#Crossfit_Athletes_2020.insert(20, column="BMI", value='height'*'weight')#

# Creating a function - create a function that helps to clean the data - replaces the NaN with blanks#


# create visual using Matplotlib#

#create visual using Seaborn#