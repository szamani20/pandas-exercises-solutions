import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.expand_frame_repr', False)

# Step 2
raw_table = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
             'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
             'female': [0, 1, 1, 0, 1],
             'age': [42, 52, 36, 24, 73],
             'preTestScore': [4, 24, 31, 2, 3],
             'postTestScore': [25, 94, 57, 62, 70]}

df = pd.DataFrame(data=raw_table)
print(df.head())

# # Step 3
# plt.scatter(y=df['preTestScore'], x=df['postTestScore'], s=df['age'])
# plt.ylabel('PreTest Score')
# plt.xlabel('PostTest Score')

# Step 4
# There is no color associated with gender, so we use this online tool:
# https://www.random.org/colors/hex
colors = ['#46b650' if female == 0 else '#30849a' for female in df['female']]
plt.scatter(y=df['preTestScore'], x=df['postTestScore'], s=4.5 * df['postTestScore'], c=colors)
plt.ylabel('PreTest Score')
plt.xlabel('PostTest Score')

# plt.savefig('scores_scatter2.png')
# plt.show()
