import pandas as pd
import numpy as np

Crossfit_Athletes_2020 = pd.read_csv('TwentyTwenty_opens_athletes.csv')
Crossfit_Athletes_2020_Scores = pd.read_csv('2020_opens_scores.csv')

print(Crossfit_Athletes_2020.columns)

Crossfit_Athletes_2020.set_index("competitorid")

Crossfit_Athletes_2020.sort_index("competitorid")

print(Crossfit_Athletes_2020)


#Crossfit_Athletes_2020['competitorid'] = Crossfit_Athletes_2020.index#



#print(Crossfit_Athletes_2020['height'])#
#print(Crossfit_Athletes_2020['weight'])#



#Crossfit_Athletes_2020.insert(20, column="BMI", value='height'*'weight')#




