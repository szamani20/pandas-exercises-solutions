import pandas as pd
import numpy as np

pd.set_option('display.expand_frame_repr', False)

DATASET_PATH = '../../dataset/student-mat.csv'

# Step 3
df = pd.read_csv(DATASET_PATH)
print(df.head())
print()

# Step 4
df = df.loc[:, 'school': 'guardian']
print(df.head())
print()

# Step 5
capitalizer = lambda x: x.upper()

# Step 6
df['Mjob'] = df['Mjob'].apply(capitalizer)
df['Fjob'] = df['Fjob'].apply(capitalizer)
print(df.head())
print()

# Step 7
print(df.tail())
print()


# Step 8
# Nah bro, I applied the result into the columns

# Step 9
def majority(age):
    return True if age >= 17 else False


df['legal_drinker'] = pd.Series([majority(age) for age in df['age']])
print(df.head())
print()

# Step 10
print(df.applymap(lambda x: x * 10 if type(x) == int else x).head())
print()
