import pandas as pd
import numpy as np

pd.set_option('display.expand_frame_repr', False)

raw_data = {
    'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons',
                 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
    'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd'],
    'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
    'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
    'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
    'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
    'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
    'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
    'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
    'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon',
               'Wyoming', 'Louisana', 'Georgia']}

# Step 3
army = pd.DataFrame(data=raw_data)
print(army.head())
print()

# Step 4
army.set_index('origin', inplace=True)
print(army.head())
print()

# Step 5
print(army['veterans'])
print()

# Step 6
print(army.loc[:, ['veterans', 'deaths']])
print()

# Step 7
print(army.columns)
print()

# Step 8
print(army.loc[['Maine', 'Alaska'], ['deaths', 'size', 'deserters']])
print()

# Step 9
print(army.iloc[3:7, 3:6])
print()

# Step 10
print(army.iloc[3:, ])
print()

# Step 11
print(army.iloc[:3, ])
print()

# Step 12
print(army.iloc[:, 4: 6])
print()

# Step 13
print(army[army['deaths'] > 50])
print()

# Step 14
print(army[army['deaths'].between(50, 500)])
print()

# Step 15
print(army[army['regiment'] != 'Dragoons'])
print()

# Step 16
print(army.loc[['Texas', 'Arizona'], ])
print()

# Step 17
# adding the [] around iloc parameters will cause to return a full cell instead of the value
print(army.loc['Arizona', army.columns[2]])
print()
print(army.loc[['Arizona'], ['deaths']])
print()

# Step 18
print(army.iloc[[2], army.columns.get_loc('deaths')])
print()
