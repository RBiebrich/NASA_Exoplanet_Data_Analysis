# NASA Exoplanet Data Analysis
### CMPS530 | Final Project 
This repo contains the code for my processing, cleaning, and analysis of data from [NASA's Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS&constraint=default_flag=1&constraint=disc_facility+like+%27%25TESS%25%27) database.


### Table Column Schema:

###### pl_name:        Planet Name
###### hostname:       Host Name
###### sy_snum:        Number of Stars
###### sy_pnum:        Number of Planets
###### sy_mnum:        Number of Moons
###### cb_flag:        Circumbinary Flag
###### discoverymethod: Discovery Method
###### disc_year:      Discovery Year
###### disc_facility:  Discovery Facility
###### disc_instrument: Discovery Instrument
###### pl_orbper:      Orbital Period [days]
###### pl_orbpererr1:  Orbital Period Upper Unc. [days]
###### pl_orbpererr2:  Orbital Period Lower Unc. [days]
###### pl_orbperlim:   Orbital Period Limit Flag
###### pl_orbsmax:     Orbit Semi-Major Axis [au])
###### pl_orbsmaxerr1: Orbit Semi-Major Axis Upper Unc. [au]
###### pl_orbsmaxerr2: Orbit Semi-Major Axis Lower Unc. [au]
###### pl_orbsmaxlim:  Orbit Semi-Major Axis Limit Flag
###### pl_rade:        Planet Radius [Earth Radius]
###### pl_radeerr1:    Planet Radius Upper Unc. [Earth Radius]
###### pl_radeerr2:    Planet Radius Lower Unc. [Earth Radius]
###### pl_radelim:     Planet Radius Limit Flag
###### pl_radj:        Planet Radius [Jupiter Radius]
###### pl_radjerr1:    Planet Radius Upper Unc. [Jupiter Radius]
###### pl_radjerr2:    Planet Radius Lower Unc. [Jupiter Radius]
###### pl_radjlim:     Planet Radius Limit Flag
###### pl_bmasse:      Planet Mass or Mass*sin(i) [Earth Mass]
###### pl_bmasseerr1:  Planet Mass or Mass*sin(i) [Earth Mass] Upper Unc.
###### pl_bmasseerr2:  Planet Mass or Mass*sin(i) [Earth Mass] Lower Unc.
###### pl_bmasselim:   Planet Mass or Mass*sin(i) [Earth Mass] Limit Flag
###### pl_bmassj:      Planet Mass or Mass*sin(i) [Jupiter Mass]
###### pl_bmassjerr1:  Planet Mass or Mass*sin(i) [Jupiter Mass] Upper Unc.
###### pl_bmassjerr2:  Planet Mass or Mass*sin(i) [Jupiter Mass] Lower Unc.
###### pl_bmassjlim:   Planet Mass or Mass*sin(i) [Jupiter Mass] Limit Flag
###### pl_bmassprov:   Planet Mass or Mass*sin(i) Provenance
###### pl_orbeccen:    Eccentricity
###### pl_orbeccenerr1: Eccentricity Upper Unc.
###### pl_orbeccenerr2: Eccentricity Lower Unc.
###### pl_orbeccenlim: Eccentricity Limit Flag
###### pl_insol:       Insolation Flux [Earth Flux]
###### pl_insolerr1:   Insolation Flux Upper Unc. [Earth Flux]
###### pl_insolerr2:   Insolation Flux Lower Unc. [Earth Flux]
###### pl_insollim:    Insolation Flux Limit Flag
###### pl_eqt:         Equilibrium Temperature [K]
###### pl_eqterr1:     Equilibrium Temperature Upper Unc. [K]
###### pl_eqterr2:     Equilibrium Temperature Lower Unc. [K]
###### pl_eqtlim:      Equilibrium Temperature Limit Flag
###### ttv_flag:       Data show Transit Timing Variations
###### st_spectype:    Spectral Type
###### st_teff:        Stellar Effective Temperature [K]
###### st_tefferr1:    Stellar Effective Temperature Upper Unc. [K]
###### st_tefferr2:    Stellar Effective Temperature Lower Unc. [K]
###### st_tefflim:     Stellar Effective Temperature Limit Flag
###### st_rad:         Stellar Radius [Solar Radius]
###### st_raderr1:     Stellar Radius Upper Unc. [Solar Radius]
###### st_raderr2:     Stellar Radius Lower Unc. [Solar Radius]
###### st_radlim:      Stellar Radius Limit Flag
###### st_mass:        Stellar Mass [Solar mass]
###### st_masserr1:    Stellar Mass Upper Unc. [Solar mass]
###### st_masserr2:    Stellar Mass Lower Unc. [Solar mass]
###### st_masslim:     Stellar Mass Limit Flag
###### st_met:         Stellar Metallicity [dex]
###### st_meterr1:     Stellar Metallicity Upper Unc. [dex]
###### st_meterr2:     Stellar Metallicity Lower Unc. [dex]
###### st_metlim:      Stellar Metallicity Limit Flag
###### st_metratio:    Stellar Metallicity Ratio
###### st_logg:        Stellar Surface Gravity [log10(cm/s**2)]
###### st_loggerr1:    Stellar Surface Gravity Upper Unc. [log10(cm/s**2)]
###### st_loggerr2:    Stellar Surface Gravity Lower Unc. [log10(cm/s**2)]
###### st_logglim:     Stellar Surface Gravity Limit Flag
###### st_age:         Stellar Age [Gyr]
###### st_ageerr1:     Stellar Age Upper Unc. [Gyr]
###### st_ageerr2:     Stellar Age Lower Unc. [Gyr]
###### st_agelim:      Stellar Age Limit Flag
###### sy_dist:        Distance [pc]
###### sy_disterr1:    Distance [pc] Upper Unc
###### sy_disterr2:    Distance [pc] Lower Unc