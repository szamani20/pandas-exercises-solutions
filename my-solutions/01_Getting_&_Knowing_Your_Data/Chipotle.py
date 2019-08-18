# I am not happy with jupyter notebook, real projects with big scale
# dataset and files, cannot be loaded and synced properly with jupyter
# so I use PyCharm IDE.

# Step 1
import pandas as pd
import numpy as np

pd.set_option('display.expand_frame_repr', False)

DATASET_PATH = '../../dataset/chipotle.tsv'

# Step 2, 3
chipo = pd.read_csv(DATASET_PATH, delimiter='\t')

# Step 4
print(chipo.head(10))
print()

# Step 5
print(chipo.info())
print()
print(chipo.shape)

# Step 6
print(chipo.shape[1])
print()

# Step 7
print(list(chipo.columns))
print()

# Step 8
print(chipo.index)
print()

# Step 9
# It's more efficient than sorting the entire column
print(chipo.groupby('item_name').count().iloc[:, 1].idxmax())
print()

# Step 10
print(chipo.groupby('item_name').count().max()['quantity'])
print()

# Step 11
print(chipo.groupby('choice_description').count().iloc[:, 1].idxmax())
print()

# Step 12
print(chipo.iloc[:, 1].sum())
print()

# Step 13
print(chipo.iloc[:, 4].dtype)
chipo.item_price = chipo.item_price.apply(lambda price: float(price[1:]))
print(chipo.item_price.dtype)
print()

# Step 14
print((chipo.quantity * chipo.item_price).sum())
print()

# Step 15
print(len(chipo.order_id.unique()))
print()

# Step 16
print((chipo.quantity * chipo.item_price).sum() / len(chipo.order_id.unique()))
print()
# I can't think of a more efficient way

# Step 17
print(len(chipo.item_name.unique()))
print()
