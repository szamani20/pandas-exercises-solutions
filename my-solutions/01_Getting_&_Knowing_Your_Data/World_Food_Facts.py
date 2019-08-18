import pandas as pd
import numpy as np

pd.set_option('display.expand_frame_repr', False)

DATASET_PATH = '../../dataset/en.openfoodfacts.org.products.tsv'

# Step 3
# food = pd.read_csv(DATASET_PATH, delimiter='\t', nrows=1000)
food = pd.read_csv(DATASET_PATH, delimiter='\t')

# Step 4
print(food.head(5))
print()

# Step 5
print(food.shape)
print()

# Step 6
print(food.shape[1])
print()

# Step 7
print(food.columns.ravel())
print()

# Step 8
print(food.columns.ravel()[104])
print()

# Step 9
print(food.iloc[:, 104].dtype)
print(food.dtypes[food.columns.ravel()[104]])
print()

# Step 10
print(food.index)
print()

# Step 11
print(food.iloc[18, :].product_name)
print()
