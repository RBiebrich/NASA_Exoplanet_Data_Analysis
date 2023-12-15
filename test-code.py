import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

raw_data = pd.read_csv('NASA-Exoplanet-Archive.csv', sep=',')
data = pd.DataFrame(raw_data.groupby('pl_name').first()).reset_index()

# ================================================================================
# SUPERLATIVES
ordered_by_disc_year = data.sort_values('disc_year')[['pl_name', 'disc_year']]
# PSR B1257+12 c: 1992

group_by_instrument = data.groupby('disc_instrument').count()
most_successful_instrument = group_by_instrument.sort_values('pl_name', ascending=False)['pl_name']
# Kepler CCD Array: 3326


def discoveries_per_instrument():
    x = list(most_successful_instrument.head(5).index)
    y = most_successful_instrument.head(5)
    colors = [(0.0, 0.4, 0.4, 0.9), (0.0, 0.4, 0.4, 0.6),
              (0.0, 0.4, 0.4, 0.4), (0.0, 0.4, 0.4, 0.3), 
               (0.0, 0.4, 0.4, 0.2)]

    fig, ax = plt.subplots()
    ax.bar(x, y, color=colors)
    plt.xlabel('Instrument')
    plt.ylabel('Number of Discoveries')
    plt.title('Exoplanet Discoveries by Instrument')
    plt.xticks(rotation=10)

    plt.show()


group_by_methods = data.groupby('discoverymethod').count()
best_method = group_by_methods.sort_values('pl_name', ascending=False)['pl_name']
# Transit: 4146


def best_methods_graph():
    x = list(best_method.head(5).index)
    y = best_method.head(5)
    colors = [(0.9, 0.1, 0.0, 0.9), (0.9, 0.2, 0.0, 0.6),
              (0.9, 0.3, 0.0, 0.4), (0.9, 0.4, 0.0, 0.3),
              (0.9, 0.5, 0.0, 0.2)]

    fig, ax = plt.subplots()
    ax.bar(x, y, color=colors)
    plt.xlabel('Method')
    plt.ylabel('Number of Discoveries')
    plt.title('Exoplanet Discoveries by Method')
    plt.xticks(rotation=20)

    plt.show()


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


kepler_filter = data['disc_instrument'] == 'Kepler CCD Array'
kepler_disc_per_year = data[kepler_filter].groupby('disc_year').count()['pl_name']

not_kepler_filter = data['disc_instrument'] != 'Kepler CCD Array'
not_kepler_disc_per_year = data[not_kepler_filter].groupby('disc_year').count()['pl_name']

def kepler():

    x1 = list(kepler_disc_per_year.index)
    y1 = kepler_disc_per_year

    x2 = list(not_kepler_disc_per_year.index)
    y2 = not_kepler_disc_per_year

    fig, ax = plt.subplots()
    ax.bar(x1, y1)
    ax.bar(x2, y2, color='red')
    plt.xlabel('Year')
    plt.ylabel('Number of Discoveries')
    plt.title('Exoplanet Discoveries by Year: Kepler vs. All Other Instruments')
    plt.legend(['Kepler', 'Other Intruments'])

    plt.show()


# discoveries_per_year_plot()
# discoveries_per_instrument()
# best_methods_graph()
# kepler()
