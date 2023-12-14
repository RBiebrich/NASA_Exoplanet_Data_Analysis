import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

raw_data = pd.read_csv('NASA-Exoplanet-Archive.csv', sep=',')
data = pd.DataFrame(raw_data.groupby('pl_name').first()).reset_index()

# Superlatives
ordered_by_disc_year = data.sort_values('disc_year')[['pl_name', 'disc_year']]
# PSR B1257+12 c: 1992

unsorted = data.groupby('disc_instrument').count()
most_successful_spacecraft = unsorted.sort_values('pl_name', ascending=False)['pl_name']
# Kepler CCD Array: 3326

farthest = data.sort_values('sy_dist', ascending=False)[['pl_name', 'sy_dist']]
# MOA-2020-BLG-135L b: 8300.0 pc

closest = data.sort_values('sy_dist')[['pl_name', 'sy_dist']]
# Proxima Cen b: 1.30119 pc

discoveries_per_year = data.groupby('disc_year').count()
biggest_year = discoveries_per_year.sort_values('pl_name', ascending=False)['pl_name']
# 2016: 1517

def discoveries_per_year_plot():
    plt.plot(discoveries_per_year['pl_name'])
    plt.xlabel('Year')
    plt.ylabel('Number of Discoveries')
    plt.title('Exoplanet Discoveries Per Year')

    plt.show()


discoveries_per_year_plot()
