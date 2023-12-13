import pandas as pd

raw_data = pd.read_csv('NASA-Exoplanet-Archive.csv', sep=',')
data = pd.DataFrame(raw_data.groupby('pl_name').first()).reset_index()
print(data)
