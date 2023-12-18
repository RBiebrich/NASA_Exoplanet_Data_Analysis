# NASA Exoplanet Data Analysis
### CMPS530 | Final Project 
This repo contains the code for my processing, cleaning, and analysis of data from [NASA's Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS&constraint=default_flag=1&constraint=disc_facility+like+%27%25TESS%25%27) database.


### Table Column Schema:


##### COLUMN pl_name:        Planet Name
##### COLUMN hostname:       Host Name
##### COLUMN sy_snum:        Number of Stars
##### COLUMN sy_pnum:        Number of Planets
##### COLUMN sy_mnum:        Number of Moons
##### COLUMN cb_flag:        Circumbinary Flag
##### COLUMN discoverymethod: Discovery Method
##### COLUMN disc_year:      Discovery Year
##### COLUMN disc_facility:  Discovery Facility
##### COLUMN disc_telescope: Discovery Telescope
##### COLUMN disc_instrument: Discovery Instrument
##### COLUMN pl_orbper:      Orbital Period [days]
##### COLUMN pl_orbpererr1:  Orbital Period Upper Unc. [days]
##### COLUMN pl_orbpererr2:  Orbital Period Lower Unc. [days]
##### COLUMN pl_orbperlim:   Orbital Period Limit Flag
##### COLUMN pl_orbsmax:     Orbit Semi-Major Axis [au])
##### COLUMN pl_orbsmaxerr1: Orbit Semi-Major Axis Upper Unc. [au]
##### COLUMN pl_orbsmaxerr2: Orbit Semi-Major Axis Lower Unc. [au]
##### COLUMN pl_orbsmaxlim:  Orbit Semi-Major Axis Limit Flag
##### COLUMN pl_rade:        Planet Radius [Earth Radius]
##### COLUMN pl_radeerr1:    Planet Radius Upper Unc. [Earth Radius]
##### COLUMN pl_radeerr2:    Planet Radius Lower Unc. [Earth Radius]
##### COLUMN pl_radelim:     Planet Radius Limit Flag
##### COLUMN pl_radj:        Planet Radius [Jupiter Radius]
##### COLUMN pl_radjerr1:    Planet Radius Upper Unc. [Jupiter Radius]
##### COLUMN pl_radjerr2:    Planet Radius Lower Unc. [Jupiter Radius]
##### COLUMN pl_radjlim:     Planet Radius Limit Flag
##### COLUMN pl_bmasse:      Planet Mass or Mass*sin(i) [Earth Mass]
##### COLUMN pl_bmasseerr1:  Planet Mass or Mass*sin(i) [Earth Mass] Upper Unc.
##### COLUMN pl_bmasseerr2:  Planet Mass or Mass*sin(i) [Earth Mass] Lower Unc.
##### COLUMN pl_bmasselim:   Planet Mass or Mass*sin(i) [Earth Mass] Limit Flag
##### COLUMN pl_bmassj:      Planet Mass or Mass*sin(i) [Jupiter Mass]
##### COLUMN pl_bmassjerr1:  Planet Mass or Mass*sin(i) [Jupiter Mass] Upper Unc.
##### COLUMN pl_bmassjerr2:  Planet Mass or Mass*sin(i) [Jupiter Mass] Lower Unc.
##### COLUMN pl_bmassjlim:   Planet Mass or Mass*sin(i) [Jupiter Mass] Limit Flag
##### COLUMN pl_orbeccen:    Eccentricity
##### COLUMN pl_orbeccenerr1: Eccentricity Upper Unc.
##### COLUMN pl_orbeccenerr2: Eccentricity Lower Unc.
##### COLUMN pl_orbeccenlim: Eccentricity Limit Flag
##### COLUMN pl_insol:       Insolation Flux [Earth Flux]
##### COLUMN pl_insolerr1:   Insolation Flux Upper Unc. [Earth Flux]
##### COLUMN pl_insolerr2:   Insolation Flux Lower Unc. [Earth Flux]
##### COLUMN pl_insollim:    Insolation Flux Limit Flag
##### COLUMN pl_eqt:         Equilibrium Temperature [K]
##### COLUMN pl_eqterr1:     Equilibrium Temperature Upper Unc. [K]
##### COLUMN pl_eqterr2:     Equilibrium Temperature Lower Unc. [K]
##### COLUMN pl_eqtlim:      Equilibrium Temperature Limit Flag
##### COLUMN st_refname:     Stellar Parameter Reference
##### COLUMN st_spectype:    Spectral Type
##### COLUMN st_teff:        Stellar Effective Temperature [K]
##### COLUMN st_tefferr1:    Stellar Effective Temperature Upper Unc. [K]
##### COLUMN st_tefferr2:    Stellar Effective Temperature Lower Unc. [K]
##### COLUMN st_tefflim:     Stellar Effective Temperature Limit Flag
##### COLUMN st_rad:         Stellar Radius [Solar Radius]
##### COLUMN st_raderr1:     Stellar Radius Upper Unc. [Solar Radius]
##### COLUMN st_raderr2:     Stellar Radius Lower Unc. [Solar Radius]
##### COLUMN st_radlim:      Stellar Radius Limit Flag
##### COLUMN st_mass:        Stellar Mass [Solar mass]
##### COLUMN st_masserr1:    Stellar Mass Upper Unc. [Solar mass]
##### COLUMN st_masserr2:    Stellar Mass Lower Unc. [Solar mass]
##### COLUMN st_masslim:     Stellar Mass Limit Flag
##### COLUMN st_met:         Stellar Metallicity [dex]
##### COLUMN st_meterr1:     Stellar Metallicity Upper Unc. [dex]
##### COLUMN st_meterr2:     Stellar Metallicity Lower Unc. [dex]
##### COLUMN st_metlim:      Stellar Metallicity Limit Flag
##### COLUMN st_metratio:    Stellar Metallicity Ratio
##### COLUMN st_lum:         Stellar Luminosity [log(Solar)]
##### COLUMN st_lumerr1:     Stellar Luminosity Upper Unc. [log(Solar)]
##### COLUMN st_lumerr2:     Stellar Luminosity Lower Unc. [log(Solar)]
##### COLUMN st_lumlim:      Stellar Luminosity Limit Flag
##### COLUMN st_logg:        Stellar Surface Gravity [log10(cm/s**2)]
##### COLUMN st_loggerr1:    Stellar Surface Gravity Upper Unc. [log10(cm/s**2)]
##### COLUMN st_loggerr2:    Stellar Surface Gravity Lower Unc. [log10(cm/s**2)]
##### COLUMN st_logglim:     Stellar Surface Gravity Limit Flag
##### COLUMN sy_dist:        Distance [pc]
##### COLUMN sy_disterr1:    Distance [pc] Upper Unc
##### COLUMN sy_disterr2:    Distance [pc] Lower Unc