import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea

Crossfit_Athletes_2020 = pd.read_csv('TwentyTwenty_opens_athletes.csv')
Crossfit_Athletes_2020_Scores = pd.read_csv('2020_opens_scores.csv')

print(Crossfit_Athletes_2020.info)
print(Crossfit_Athletes_2020.columns)
print(Crossfit_Athletes_2020_Scores.columns)


Crossfit_Athletes_2020["height_squared"] = Crossfit_Athletes_2020["height"]**2
Crossfit_Athletes_2020['BMI'] = Crossfit_Athletes_2020["weight"] / Crossfit_Athletes_2020["height_squared"]

Crossfit_Athletes_2020['BMI'] = np.where((Crossfit_Athletes_2020.BMI <1),'0',Crossfit_Athletes_2020.BMI)


print(Crossfit_Athletes_2020.columns)

Crossfit_Athletes_2020_Scores.set_index("competitorid")

Crossfit_Athletes_2020_dropped = Crossfit_Athletes_2020.drop(columns=["profilepics3key","countryoforigincode","affiliateid","countryoforiginname","is_scaled"], axis= 1, inplace= False )

print(Crossfit_Athletes_2020_dropped.columns)

print(Crossfit_Athletes_2020_dropped.info)

Crossfitsorted =Crossfit_Athletes_2020_dropped.sort_values('overallrank')

print(Crossfitsorted)

Crossfit_Athletes_split_for_gen_female= Crossfitsorted.loc[Crossfitsorted['gender']=="F"]

Crossfit_Athletes_split_for_gen_female_dupes_removed = Crossfit_Athletes_split_for_gen_female.drop_duplicates(subset='competitorid', keep="last")

print(Crossfit_Athletes_split_for_gen_female_dupes_removed.info)
print(Crossfit_Athletes_split_for_gen_female_dupes_removed.max(axis=0)['age'])
print(Crossfit_Athletes_split_for_gen_female_dupes_removed.min(axis=0)['age'])

Crossfitsorted_for_females_byrank = Crossfit_Athletes_split_for_gen_female_dupes_removed.sort_values('overallrank')

print(Crossfitsorted_for_females_byrank)

Crossfit_Athletes_split_for_gen_male= Crossfitsorted.loc[Crossfitsorted['gender']=="M"]

Crossfit_Athletes_split_for_gen_male_dupes_removed = Crossfit_Athletes_split_for_gen_male.drop_duplicates(subset='competitorid', keep="last")

print(Crossfit_Athletes_split_for_gen_male_dupes_removed.info)

Crossfitsorted_formen_byrank = Crossfit_Athletes_split_for_gen_male_dupes_removed.sort_values('overallrank')

Crosfit_sorted_by_Age_male = Crossfit_Athletes_split_for_gen_male_dupes_removed.sort_values('age')
print(Crossfit_Athletes_split_for_gen_male_dupes_removed)
print(Crosfit_sorted_by_Age_male.max(axis=0)['age'])
print(Crosfit_sorted_by_Age_male.min(axis=0)['age'])
Count_of_Male_Competitors_2020 = Crossfit_Athletes_split_for_gen_male_dupes_removed.groupby(['competitorid']).count()
print(Count_of_Male_Competitors_2020)

print(Crosfit_sorted_by_Age_male [['competitorid','age']])

print(Crossfitsorted_formen_byrank[['division','divisionid','overallscore', 'competitorname','competitorid']])

Plot_of_Men_Athletes_Age = Crossfit_Athletes_split_for_gen_male_dupes_removed.hist(column='age', bins=15, color = "red")
plt.title("Age Distribution: Male Athletes")
plt.ylabel('Number of Athletes')
plt.xlabel('Age')
plt.show()

Plot_of_Women_Athletes_Age = Crossfit_Athletes_split_for_gen_female_dupes_removed.hist(column='age', bins=15)
plt.title("Age Distribution: Female Athletes")
plt.ylabel('Number of Athletes')
plt.xlabel('Age')
plt.show()

print(Crossfitsorted_formen_byrank[['competitorname','weight','height','divisionid']])

Crossfit_Athletes_NaN_replaced_Sorted_formales_byrank =Crossfitsorted_formen_byrank.replace(np.NaN, 0)

Crossfit_Athletes_NaN_replaced_Sorted_forfemales_byrank =Crossfitsorted_for_females_byrank.replace(np.NaN, 0)

Crossfit_2020_data_merged = pd.merge(Crossfit_Athletes_2020_Scores, Crossfit_Athletes_2020, on='competitorid')

print(Crossfit_2020_data_merged)









