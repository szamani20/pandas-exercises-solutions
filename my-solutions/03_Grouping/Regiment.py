import pandas as pd

pd.set_option('display.expand_frame_repr', False)

# Step 2
raw_data = {
    'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons',
                 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
    'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd'],
    'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani',
             'Ali'],
    'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

# Step 3
regiment = pd.DataFrame(data=raw_data)
print(regiment.head())
print()

# Step 4
print(regiment.groupby('regiment')['preTestScore'].mean().loc['Nighthawks', ])
print()

# Step 5
print(regiment.groupby('company').describe())
print()

# Step 6
print(regiment.groupby('company').preTestScore.mean())
print()

# Step 7
print(regiment.groupby(['regiment', 'company']).agg({'preTestScore': 'mean'}))
print()

# Step 8
print(regiment.groupby(['regiment', 'company']).agg({'preTestScore': 'mean'}).unstack())
print()

# Step 9
print(regiment.groupby(['regiment', 'company']).count())
print()

# Step 10
print(regiment.groupby('regiment').size())
print()
print(regiment.groupby('company').size())
print()

# Step 11
for name, group in regiment.groupby('regiment'):
    print(group)
print()
