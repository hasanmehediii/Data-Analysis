import numpy as np

ages = np.array([[21, 25, 30, 35, 40, 45, 50, 55, 60, 65],
                [39, 15, 28, 42, 55, 18, 22, 27, 33, 36]])

# Filter ages greater than 30
filter1 = ages > 30
print(ages[filter1])  # [35 40 45 50 55 60 65]

# Filter ages less than or equal to 30
filter2 = ages <= 30
print(ages[filter2])  # [21 25 30]

# Filter ages between 30 and 50 (inclusive)
filter3 = (ages >= 30) & (ages <= 50)
print(ages[filter3])  # [30 35 40 45 50]

# Filter ages less than 25 or greater than 55
filter4 = (ages < 25) | (ages > 55)
print(ages[filter4])  # [21 25 60 65]

teenagers = ages[ages < 20]
print(teenagers)  # [15 18]

adults = ages[(ages >= 20) & (ages <= 65)]
print(adults)  # [21 25 30 35 40 45 50 55 60 65]

odds = ages[ages % 2 != 0]
print(odds)  # [21 25 35 45 55 65]

evens = ages[ages % 2 == 0]
print(evens)  # [30 40 50 60]

adult = np.where(ages >= 18, 'Adult', 'Minor')
print(adult)
# ['Adult' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult'
#  'Adult' 'Minor' 'Adult' 'Adult' 'Adult' 'Adult' 'Minor' 'Adult' 'Adult
#  'Adult' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult 'Adult' 'Adult' 'Adult']
minor = np.where(ages < 18, 'Minor', 'Adult')
print(minor)
# ['Minor' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult'
#  'Adult' 'Minor' 'Adult' 'Adult' 'Adult' 'Adult' 'Minor' 'Adult' 'Adult'
#  'Adult' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult' 'Adult']