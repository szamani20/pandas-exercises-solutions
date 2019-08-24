import pandas as pd

pd.set_option('display.expand_frame_repr', False)

DATASET_PATH = '../../dataset/wind.data'

# Step 3
data = pd.read_csv(DATASET_PATH, delimiter='\s+', parse_dates=[[0, 1, 2]])
print(data.head())
print()

# Step 4
# x is of type pd.Timestamp()
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(lambda x: x.replace(year=x.year - 100) if x.year > 1989 else x)
print(data.head())
print()

# Step 5
data.set_index('Yr_Mo_Dy', drop=True, inplace=True)
print(data.head())
print()

# Step 6
print(data.isna().sum())
print()

# Step 7
print(data.notnull().sum() - data.isna().sum())
print()

# Step 8
print(data.mean(skipna=True).mean())
print()

# Step 9
loc_stats = pd.DataFrame(data={
    'min': data.min(),
    'max': data.max(),
    'mean': data.mean(skipna=True),
    'std': data.std(skipna=True),
})
print(loc_stats.head())
print()

# Step 10
day_stats = pd.DataFrame(data={
    'min': data.min(axis=1),
    'max': data.max(axis=1),
    'mean': data.mean(skipna=True, axis=1),
    'std': data.std(skipna=True, axis=1),
}, index=data.index)
print(day_stats.head())
print()

# Step 11
print(data[data.index.month == 1].mean())
print()

# Step 12
print(data.resample('Y').mean())
print()

# Step 13
print(data.resample('M').mean())
print()

# Step 14
print(data.resample('W').mean())
print()

# Step 15
print(data.resample('W').agg(['min', 'max', 'mean', 'std'], skipna=True).iloc[1:53, ].head())
print()
