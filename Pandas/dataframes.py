import pandas as pd

data = {
    'Name': ['Spongebob', 'Patrick', 'Charlie', 'David', 'Messi'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data, index=['#1', '#2', '#3', '#4', '#5'])
print(df)
print(df.loc['#5'])

print(df.iloc[4])

# Add new column
df["Country"] = ['USA', 'USA', 'USA', 'USA', 'Argentina']
print(df)

# Add new row
new_row = pd.DataFrame({
    'Name': ['Neymar'],
    'Age': [28],
    'City': ['Rio de Janeiro'],
    'Country': ['Brazil']
}, index=['#6'])
df = pd.concat([df, new_row])
print(df)

# Add new rows
new_rows = pd.DataFrame({
    'Name': ['Kylian', 'Mbappe'],
    'Age': [23, 24],
    'City': ['Paris', 'Paris'],
    'Country': ['France', 'France']
}, index=['#7', '#8'])
df = pd.concat([df, new_rows])
print(df)