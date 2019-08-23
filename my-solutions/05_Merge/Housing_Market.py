import pandas as pd
import numpy as np

pd.set_option('display.expand_frame_repr', False)

# Step 2
random_number = pd.Series(data=np.random.randint(low=1, high=5, size=100))
random_number2 = pd.Series(data=np.random.randint(low=1, high=4, size=100))
random_number3 = pd.Series(data=np.random.randint(low=10000, high=30000, size=100))

# Step 3
df = pd.concat([random_number, random_number2, random_number3], axis=1)
print(df.head())
print()

# Step 4
df.columns = ['bedrs', 'bathrs', 'price_sqr_meter']
print(df.head())
print()

# Step 5
bigcolumn = pd.concat([random_number, random_number2, random_number3]).to_frame()
print(bigcolumn)
print()

# Step 6, 7
bigcolumn.reset_index(inplace=True, drop=True)
# bigcolumn.drop('index', inplace=True, axis=1)
print(bigcolumn)
print()
