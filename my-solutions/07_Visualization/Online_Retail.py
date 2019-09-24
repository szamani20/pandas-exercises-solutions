import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.expand_frame_repr', False)

DATASET_PATH = '../../dataset/Online_Retail.csv'

# Step 3
# online_rl = pd.read_csv(DATASET_PATH, encoding='latin1', nrows=10000)
online_rl = pd.read_csv(DATASET_PATH, encoding='latin1')
print(online_rl.shape)
print(online_rl.head())
print()

# Step 4
# most_quantity_country = online_rl.groupby('Country').agg({'Quantity': 'sum'}).sort_values(by='Quantity',
#                                                                                           ascending=False)
# print(most_quantity_country.head())
# most_quantity_country.iloc[1:11, ].plot.bar()
# plt.xlabel('Country')
# plt.ylabel('Quantity')
# plt.title('Retail quantity per country except UK')
# print()

# # Step 5
# online_rl = online_rl[online_rl['Quantity'] >= 0]
# print(online_rl.shape)
# print()

# # Step 6
# customer_country = online_rl.groupby(['CustomerID', 'Country']).sum()
# customer_country = customer_country[customer_country['UnitPrice'] > 0]
# top_three_countries = ['United Kingdom', 'Netherlands', 'EIRE']
# # Country is in index, let's also have a copy of it as a separate column
# customer_country['Country'] = customer_country.index.get_level_values(1)
# customer_country = customer_country[customer_country['Country'].isin(top_three_countries)]
# print(customer_country.head())
# print()

# plt.show()
