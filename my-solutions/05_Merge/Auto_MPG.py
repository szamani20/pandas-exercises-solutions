import pandas as pd
import numpy as np

pd.set_option('display.expand_frame_repr', False)

DATASET_PATH1 = '../../dataset/cars1.csv'
DATASET_PATH2 = '../../dataset/cars2.csv'

# Step 3
cars1 = pd.read_csv(DATASET_PATH1)
cars2 = pd.read_csv(DATASET_PATH2)
print(cars1.head())
print()
print(cars2.head())
print()

# Step 4
cars1 = cars1.iloc[:, :9]
print(cars1.head())
print()

# Step 5
print(cars1.shape)
print(cars2.shape)
print()

# Step 6
cars = cars1.append(cars2)
print(cars.head())
print()

# Step 7, 8
cars['owners'] = pd.Series(data=np.random.randint(low=15000, high=73000, size=cars.shape[0]))
print(cars.head())
print()
