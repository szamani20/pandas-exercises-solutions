import pandas as pd

pd.set_option('display.expand_frame_repr', False)

DATASET_PATH = '../../dataset/Euro_2012_stats_TEAM.csv'

# Step 3
euro12 = pd.read_csv(DATASET_PATH)
print(euro12.head())

# Step 4
print(euro12.Goals)
print()

# Step 5
print(euro12.shape[0])
print()

# Step 6
print(euro12.shape[1])
print()

# Step 7
discipline = pd.DataFrame(data={'Team': euro12['Team'],
                                'Yellow Cards': euro12['Yellow Cards'],
                                'Red Cards': euro12['Red Cards']})
print(discipline)
print()

# Step 8
discipline.sort_values(by=['Red Cards', 'Yellow Cards'], inplace=True)
print(discipline)
print()

# Step 9
print(discipline['Yellow Cards'].mean())
print()

# Step 10
print(euro12[euro12['Goals'] > 6])
print()

# Step 11
print(euro12[euro12['Team'].str.startswith('G')])
print()
print(euro12[euro12['Team'].apply(lambda x: x.startswith('G'))])
print()

# Step 12
print(euro12.iloc[:, :7])
print()

# Step 13
print(euro12.iloc[:, :-3])
print()

# Step 14
print(euro12[euro12['Team'].apply(lambda x: x in ['England', 'Italy', 'Russia'])].loc[:, ['Team', 'Shooting Accuracy']])
print()
print(euro12.loc[euro12['Team'].isin(['England', 'Italy', 'Russia']), ['Team', 'Shooting Accuracy']])
print()
