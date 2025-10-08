import pandas as pd

# series = A Pandas 1-dimensional labeled array capable of holding any data type
# Creating a Series by passing a list of values, letting pandas create a default integer index:

data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series)

data1 = [10.3, 20.5, 30.7, 40.9, 50.1]
series1 = pd.Series(data1)
print(series1)

data2 = ['a', 'b', 'c', 'd', 'e']
series2 = pd.Series(data2)
print(series2)

data3 = [True, False, True, False, True]
series3 = pd.Series(data3)
print(series3)

data4 = [10, 'b', 30.5, True, None]
series4 = pd.Series(data4)
print(series4)

# custom index
data5 = [10, 20, 30]
series5 = pd.Series(data5, index=['apartment #1', 'apartment #2', 'apartment #3'])
print(series5)
print(series5.loc["apartment #2"])

series5.loc["apartment #3"] = 35
print(series5)
print(series5.iloc[2])
print(series5[series5 >= 20])

calories = {"Day 1": 1750, "Day 2": 1800, "Day 3": 1900}
calories_series = pd.Series(calories)
print(calories_series)
calories_series["Day 2"] += 2000
print(calories_series["Day 2"])