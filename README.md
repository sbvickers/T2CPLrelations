*********************************************** 
This module is designed to calculated absolute 
mags and distances to type II Cepheids (T2C) using 
empirical period-luminosity (PL) relations from 
Alcock et al. (1998) and Matsunaga et al. (2006).*
*********************************************** 

This module was built to be utilised with other, 
larger scripts to calculate the absolute mags and
distances of T2C's.

The module can be used by;

    import plCalc

and called either by 
    
    plCalc.calc(P, m, ebv, band)

where P is the period in days, m is the apparent magnitude,
ebv is the B-V color excess and the band is the waveband
of the apparent magnitude. Options for the waveband are
V, J, H and K. 

This function call will return the distance of the object.

To calculate the absolute magnitudes or extinction
in any of the valid wavebands then the following 
calls are valid.

    M_PL(P, band)

    or 

    A_lambda(ebv, band)

The script does not take into account any bolometric corrections as of yet.

Note: this module requires the uncertainties module to function.**

*http://adsabs.harvard.edu/abs/1998AJ....115.1921A &
http://adsabs.harvard.edu/abs/2006MNRAS.370.1979M

**https://pypi.python.org/pypi/uncertainties/

Copyright (c) 2014, Shane Vickers
All rights reserved.
