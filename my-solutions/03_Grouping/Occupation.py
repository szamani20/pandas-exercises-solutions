import pandas as pd

pd.set_option('display.expand_frame_repr', False)

DATASET_PATH = '../../dataset/u.user'

# Step 3
users = pd.read_csv(DATASET_PATH, delimiter='|')
print(users.head())
print()

# Step 4
print(users.groupby('occupation')['age'].mean())
print()
# Or with using agg() function
print(users.groupby('occupation').agg({'age': 'mean'}))
print()

# Step 5
all_gender_sum = users.groupby('occupation')['gender'].count()
male_gender = users[users['gender'] == 'M'].groupby('occupation')['gender'].count()
# No female doctor? Such a shame for the education system.
print((male_gender / all_gender_sum).sort_values(ascending=False))
print()

# Step 6
print(users.groupby('occupation').agg({'age': ['min', 'max']}))
print()

# Step 7
print(users.groupby(['occupation', 'gender']).age.mean())
print()

# Step 8
all_gender_sum = users.groupby('occupation')['gender'].count()
male_gender = users[users['gender'] == 'M'].groupby('occupation')['gender'].count()
female_gender = users[users['gender'] == 'F'].groupby('occupation')['gender'].count()
print(pd.DataFrame(data={'F': female_gender / all_gender_sum,
                         'M': male_gender / all_gender_sum},
                   index=male_gender.index))
print()
