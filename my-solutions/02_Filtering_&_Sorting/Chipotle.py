import pandas as pd

pd.set_option('display.expand_frame_repr', False)

DATASET_PATH = '../../dataset/chipotle.tsv'

# Step 3
chipo = pd.read_csv(DATASET_PATH, delimiter='\t')
print(chipo.head(10))
print()

# Step 4
chipo.item_price = chipo.item_price.apply(lambda price: float(price[1:]))
chipo2 = chipo.drop_duplicates(subset=['item_name', 'item_price'])
chipo2 = chipo2[chipo2['quantity'] == 1]
print(len(chipo2[chipo2['item_price'] > 10].item_name.unique()))
print()

# Step 5
print(chipo2[['item_name', 'item_price']].sort_values('item_price'))
print()

# Step 6
print(chipo.sort_values(by='item_name'))
print()

# Step 7
print(chipo.sort_values(by='item_price').iloc[-1, 1])
print()

# Step 8
print(chipo.item_name.value_counts()['Veggie Salad Bowl'])
print()

# Step 9
print(chipo[(chipo['item_name'] == 'Canned Soda') & (chipo['quantity'] > 1)].shape[0])
print()
