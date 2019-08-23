import pandas as pd

pd.set_option('display.expand_frame_repr', False)

DATASET_PATH = '../../dataset/US_Baby_Names_right.csv'

# Step 3, 4
baby_names = pd.read_csv(DATASET_PATH)
print(baby_names.head(10))
print()

# Step 5
baby_names.drop(['Unnamed: 0', 'Id'], axis=1, inplace=True)
print(baby_names.head())
print()

# Step 6
print(baby_names[baby_names['Gender'] == 'F'].shape[0])
print(baby_names[baby_names['Gender'] == 'M'].shape[0])
print()

# Step 7
names = baby_names.drop('Year', axis=1).groupby('Name').sum()
print(names)
print()

# Step 8
print(names.shape[0])
print(baby_names['Name'].unique().size)
print()

# Step 9
print(names.idxmax())
print()

# Step 10
print(names[names['Count'] == names['Count'].min()].shape[0])
print()

# Step 11
print(names[names['Count'] == names['Count'].median()])
print()

# Step 12
print(names['Count'].std())
print()

# Step 13
print(names.describe())
print()
