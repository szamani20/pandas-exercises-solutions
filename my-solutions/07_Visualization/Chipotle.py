import pandas as pd
import collections
import matplotlib.pyplot as plt

pd.set_option('display.expand_frame_repr', False)

DATASET_PATH = '../../dataset/chipotle.tsv'

# Step 3, 4
chipo = pd.read_csv(DATASET_PATH, sep='\t')
print(chipo.head(10))
print()

# Step 5
top_items = chipo.groupby('item_name').count().sort_values('quantity', ascending=False).iloc[:5, 1]
print(top_items)
# top_items.plot.bar()
# plt.ylabel('Quantity')
# plt.xlabel('Item')
# plt.title('Top item sells')
print()

# Step 6
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:].strip()))
order_item = chipo.groupby('order_id').sum()
print(order_item)
# plt.scatter(y=order_item['quantity'], x=order_item['item_price'])
# plt.ylabel('Quantity')
# plt.xlabel('Price')
# plt.title('Item quantity price')
print()

# plt.savefig('scatter.png')
plt.show()
