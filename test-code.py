import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.constants import gravitational_constant as G
from scipy.constants import pi

raw_data = pd.read_csv('NASA-exoplanet-archive3.csv', sep=',')
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


not_kepler_filter = data['disc_instrument'] != 'Kepler CCD Array'
not_kepler_disc_per_year = data[not_kepler_filter].groupby('disc_year').count()['pl_name']


def kepler():

    x1 = list(discoveries_per_year['pl_name'].index)
    y1 = discoveries_per_year['pl_name']

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


def extrapolate():

    x = list(not_kepler_disc_per_year.index)[:-1]
    y = list(not_kepler_disc_per_year)[:-1]
    func = interp1d(x, y, axis=0, bounds_error=False, kind='quadratic', fill_value='extrapolate')

    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Predicted Exoplanet Discoveries by Year')

    x5 = list(range(2000, 2029))
    y5 = func(x5)

    axs[0, 0].plot(x5, y5)
    axs[0, 0].plot(x, y)
    axs[0, 0].set_title('Five Years (2028)')
    axs[0, 0].legend(['Extrapolation', 'Data'])

    x10 = list(range(2000, 2034))
    y10 = func(x10)
    axs[0, 1].plot(x10, y10)
    axs[0, 1].plot(x, y)
    axs[0, 1].set_title('Ten Years (2033)')

    x50 = list(range(2000, 2074))
    y50 = func(x50)
    axs[1, 0].plot(x50, y50)
    axs[1, 0].plot(x, y)
    axs[1, 0].set_title('Fifty Years (2073)')

    x100 = list(range(2000, 2124))
    y100 = func(x100)
    axs[1, 1].plot(x100, y100)
    axs[1, 1].plot(x, y)
    axs[1, 1].set_title('One Hundred Years (2123)')

    for ax in axs.flat:
        ax.set(xlabel='Years', ylabel='Number of Discoveries')
    fig.tight_layout()

    plt.show()


# ================================================================================
# CALCULATIONS

Me = 5.9722*10**24
re = 6371000

notna_filter = data['pl_rade'].notna()


def r_in_meters():
    # Create new column for radius in meters...
    data['pl_r_meters'] = (data['pl_rade']*re)
    return data[notna_filter]['pl_r_meters']


def m_in_kg():
    # Create new column for mass in kilograms...
    data['pl_mass_kg'] = (data['pl_bmasse']*Me)
    return data[notna_filter]['pl_mass_kg']


def volume():
    r_in_meters()

    # Create new column for volume...
    data['pl_vol'] = 4/3*pi*(data['pl_r_meters'])**3
    return data[notna_filter]['pl_vol']


def density():
    m_in_kg()
    volume()

    # Create new column for mean desnity...
    data['pl_density'] = data['pl_mass_kg']/data['pl_vol']
    return data[notna_filter]['pl_density']


def density_cutoff():
    density()
    # filter out densities that do not meet our criteria
    filtered = data['pl_density'] >= 3000
    return data[filtered]


def habitable_boundaries():
    filtered = data['st_lum'].notna()
    # Create new column for surface gravity...
    data['inner_rad'] = np.sqrt((np.absolute(data['st_lum']))/1.1)

    # Create new column for surface gravity...
    data['outer_rad'] = np.sqrt((np.absolute(data['st_lum']))/0.53)

    return data[filtered]


def goldilocks_filter():
    df = habitable_boundaries()
    filtered = (df['pl_orbsmax'] >= df['inner_rad']) & (df['pl_orbsmax'] <= df['outer_rad'])
    return df[filtered]


def gravity():
    # Create new column for surface gravity...
    data['surface_g'] = G*(Me*data['pl_bmasse'])/(re*data['pl_rade'])**2
    return data[notna_filter]['surface_g']


# discoveries_per_year_plot()
# discoveries_per_instrument()
# best_methods_graph()
# kepler()
# extrapolate()
# r_in_meters()
# print(gravity())
# print(density())
# print(density_cutoff())
# print(habitable_boundaries())
# print(goldilocks_filter())
