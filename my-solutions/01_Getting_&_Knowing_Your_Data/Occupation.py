import pandas as pd

pd.set_option('display.expand_frame_repr', False)

DATASET_PATH = '../../dataset/u.user'

# Step 3
user = pd.read_csv(DATASET_PATH, delimiter='|', index_col='user_id')

# Step 4
print(user.head(25))
print()

# Step 5
print(user.tail(10))
print()

# Step 6
print(user.shape)
print()

# Step 7
print(user.shape[1])
print()

# Step 8
print(user.columns.ravel())
print()

# Step 9
print(user.index)
print()

# Step 10
print(user.dtypes)
print()

# Step 11
print(user.loc[:, 'occupation'])
print()

# Step 12
print(len(user.loc[:, 'occupation'].unique()))
print()

# Step 13
print(user.groupby('occupation').count().idxmax())
print(user.groupby('occupation').count().max())
print()

# Step 14
print(user.describe())
print()

# Step 15
print(user.describe(include='all'))
print()

# Step 16
print(user.occupation.describe())
print()

# Step 17
print(user.age.mean())
print()

# Step 18
print(user.age.value_counts().tail())
print()
