import pandas as pd

pd.set_option('display.expand_frame_repr', False)

DATASET_PATH = '../../dataset/drinks.csv'

# Step 3
# NA here means North America, not NaN or null value
drinks = pd.read_csv(DATASET_PATH, na_values=['NaN', 'NAN'], keep_default_na=False)
print(drinks.head())
print()

# Step 4
print(drinks.groupby('continent')['beer_servings'].sum().idxmax())
print()

# Step 5
print(drinks.groupby('continent')['wine_servings'].describe())
print()

# Step 6
print(drinks.groupby('continent').mean())
print()

# Step 7
print(drinks.groupby('continent').median())
print()

# Step 8
print(drinks.groupby('continent')['spirit_servings'].agg(['mean', 'min', 'max']))
print()
