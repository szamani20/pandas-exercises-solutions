import pandas as pd

pd.set_option('display.expand_frame_repr', False)

raw_data_1 = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
raw_data_2 = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
raw_data_3 = {
    'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
    'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

# Step 3
data1 = pd.DataFrame(data=raw_data_1)
data2 = pd.DataFrame(data=raw_data_2)
data3 = pd.DataFrame(data=raw_data_3)

# Step 4
all_data = data1.append(data2)
print(all_data.head(10))
print()

# Step 5
all_data_col = pd.concat([data1, data2], axis=1)
print(all_data_col.head())
print()

# Step 6
print(data3.head(10))
print()

# Step 7
print(pd.merge(all_data, data3, on='subject_id'))
print()

# Step 8
print(pd.merge(data1, data2, on='subject_id', suffixes=('_1', '_2')).head(10))
print()

# Step 9
print(pd.merge(data1, data2, on='subject_id', how='outer').head(10))
print()
