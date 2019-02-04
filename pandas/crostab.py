import pandas as pd


df1 = pd.read_csv('files/survey-hand.csv')

# Prints hand by country
print(pd.crosstab(df1.country,df1.hand))
# Prints handedness by sex
print(pd.crosstab(df1['sex'],df1['hand']))
# Prints handedness by sex by country
print(pd.crosstab([df1.country,df1.sex], df1.hand))
# Prints handedness by sex by country and add totals
print(pd.crosstab([df1.country,df1.sex], df1.hand, margins=True))

# Getting percentages
print(pd.crosstab(df1['sex'],df1['hand'], normalize='index'))


# Get average age of left handed males
print(pd.crosstab(df1.sex,df1.hand, values=df1.age, aggfunc='mean'))