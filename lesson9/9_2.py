import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')

df[df['population']==df['population'].min()]['households'].max()