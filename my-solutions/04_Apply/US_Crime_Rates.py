import pandas as pd

pd.set_option('display.expand_frame_repr', False)

DATASET_PATH = '../../dataset/US_Crime_Rates_1960_2014.csv'

# Step 3
crime = pd.read_csv(DATASET_PATH)
print(crime.head())
print()

# Step 4
print(crime.dtypes)
print()

# Step 5
crime['Year'] = pd.to_datetime(crime['Year'], format='%Y')

# Step 6
crime.set_index('Year', drop=True, inplace=True)
print(crime.head())
print()

# Step 7
crime.drop(labels='Total', axis=1, inplace=True)
print(crime.head())
print()

# Step 8
crime = crime.resample('10Y').sum()
print(crime.head())
print()

# Step 9
print(crime.idxmax())
print()
