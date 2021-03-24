import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Crossfit_Athletes_2020 = pd.read_csv('TwentyTwenty_opens_athletes.csv')
Crossfit_Athletes_2020_Scores = pd.read_csv('2020_opens_scores.csv')

print(Crossfit_Athletes_2020.columns)
print(Crossfit_Athletes_2020_Scores.columns)


Crossfit_Athletes_2020["height_squared"] = Crossfit_Athletes_2020["height"]**2
Crossfit_Athletes_2020['BMI'] = Crossfit_Athletes_2020["weight"] / Crossfit_Athletes_2020["height_squared"]

print(Crossfit_Athletes_2020.columns)

Crossfit_Athletes_2020_Scores.set_index("competitorid")

Crossfit_Athletes_2020_dropped = Crossfit_Athletes_2020.drop(columns=["profilepics3key","countryoforigincode","affiliateid","countryoforiginname","is_scaled"], axis= 1, inplace= False )

print(Crossfit_Athletes_2020_dropped.columns)

Crossfit_Athletes_2020_dropped.set_index("competitorid")

Crossfitsorted =Crossfit_Athletes_2020_dropped.sort_values('overallrank')

print(Crossfitsorted)

Crossfit_Athletes_split_for_div_Women= Crossfitsorted.loc[Crossfitsorted['division']=="Women"]

Crossfit_Athletes_split_for_div_Women_dupes_removed = Crossfit_Athletes_split_for_div_Women.drop_duplicates(subset='competitorid', keep="last")

Crossfitsorted_for_women_byrank = Crossfit_Athletes_split_for_div_Women_dupes_removed.sort_values('overallrank')

print(Crossfitsorted_for_women_byrank)

Crossfit_Athletes_split_for_div_Men= Crossfitsorted.loc[Crossfitsorted['division']=="Men"]

Crossfit_Athletes_split_for_div_Men_dupes_removed = Crossfit_Athletes_split_for_div_Men.drop_duplicates(subset='competitorid', keep="last")

Crossfitsorted_formen_byrank = Crossfit_Athletes_split_for_div_Men_dupes_removed.sort_values('overallrank')

Crosfit_sorted_by_Age_men = Crossfit_Athletes_split_for_div_Men.sort_values('age')

print(Crosfit_sorted_by_Age_men [['competitorid','age']])

print(Crossfitsorted_formen_byrank[['division','divisionid','overallscore', 'competitorname','competitorid']])

Plot_of_Men_Athletes_Age = Crossfit_Athletes_split_for_div_Men.hist(column='age', bins=15, color = "red")
plt.title("Age Distribution: Men")

plt.show()

Plot_of_Women_Athletes_Age = Crossfit_Athletes_split_for_div_Women.hist(column='age', bins=15)
plt.title("Age Distribution: Women")

plt.show()


print(Crossfit_Athletes_split_for_div_Women.columns)

print(Crossfitsorted_formen_byrank[['competitorname','weight','height','divisionid']])

Crossfit_Athletes_NaN_replaced_Sorted_formen_byrank =Crossfitsorted_formen_byrank.replace(np.NaN, 0)

print(Crossfit_Athletes_NaN_replaced_Sorted_formen_byrank[['competitorname','weight','height','divisionid']])

Crossfit_Athletes_2020_men_rank_reverse_order = Crossfit_Athletes_NaN_replaced_Sorted_formen_byrank.sort_values('overallrank',  ascending=False)

#plt.scatter(x=Crossfit_Athletes_2020_men_rank_reverse_order['overallrank'], y=Crossfit_Athletes_2020_men_rank_reverse_order['BMI'])#

#plt.show()#













