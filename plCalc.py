import numpy as np

try:
    from uncertainties import ufloat
except ImportError as e:
    print( "Uncertainties package not found. Uncertainties package must be installed to use this module." )

def M_PL(P, band):
    """
        Calculates absolute magnitude using the period-luminosity
        relation of Alcock et al. (1998) and Matsunaga et al. (2006)

        Parameters
        ---------
                P : float
                The Pulsation period of the object.

                band : string
                The band defining which PL relation to use.
                From B, J, H and K.

        Returns
        ---------
                M_lambda : ufloat
                The absolute J-band magnitude of the object.
    """

    if 'J' in band:
        return ufloat(-2.23,0.05) * (np.log10(P) - 1.2) - ufloat(3.54,0.03)
    elif 'H' in band:
        return ufloat(-2.34,0.05) * (np.log10(P) - 1.2) - ufloat(3.94,0.02)
    elif 'K' in band:
        return ufloat(-2.41,0.05) * (np.log10(P) - 1.2) - ufloat(4.00,0.02)
    elif 'V' in band:
        return ufloat(2.54,0.48) - ufloat(3.91,0.36) * np.log10(P)

def A_lambda(ebv, band):
    """
        Calculates Extinction A_lambda for a given waveband where 'band'
        defines the method of calculating A_lambda.

        Parameters
        ---------
                ebv : ufloat
                The B-V color excess for the given object.

                band : string
                The waveband to calculate A_lambda.

        Returns
        ---------
                A_lambda : ufloat
                The extinction in magnitudes for the waveband lambda.
    """

    if 'J' in band:
        return ebv * 0.866
    elif 'H' in band:
        return ebv * 0.565
    elif 'K' in band:
        return ebv * 0.365
    elif 'V' in band:
        return ebv * 3.086

def dist(m, M, A):
    """
        Calculates the distance using the distance modulus.

        Parameters
        ---------
                m : ufloat
                The apparent magnitude of the object.

                M : ufloat
                The absolute magnitude of the object.

                A : ufloat
                The extinction in magnitudes in the line of sight of the object.

        Returns
        ---------
                d : ufloat
                The distance of the object in kpc
    """
    return 10**((m - M - A)/5 + 1) / 1000

def calc(P, m, ebv, band, verbose=True):
    """
        Calculates the distance using the distance modulus.

        Parameters
        ---------
                P : float
                The period of pulsation of the star.

                m : ufloat or list
                The apparent magnitude of the object or a list of magnitudes 
                [V, J, H, K]

                ebv : ufloat
                The Color excess of the object.

                band : string
                If no band is defined then all bands are calculated assuming 
                m is a list of apparent magnitudes [V, J, H, K]

                verbose : bool, optional
                Determines whether or not to print a summary of the data.

        Returns
        ---------
                d : ufloat
                The distance of the object in kpc
    """
    try:
        m.n, ebv.n
    except AttributeError as e:
        print( "Apparent magnitude (m) and color excess (ebv) must be ufloats." )
        return None

    M = M_PL(P, band)
    A = A_lambda(ebv, band)
    d = dist(m, M, A)

    if verbose:
        print( "Pulsation Period = {:.1F} days".format(P) )
        print( "Apparent {}-Band Magnitude = {:.2F}+-{:.2F} mag".format(band, m.n, m.s) )
        print( "Absolute {}-Band Magnitude = {:.2F}+-{:.2F} mag".format(band, M.n, M.s) )
        print( "Distance = {:.1F}+-{:.1F} kpc".format(d.n, d.s) )

    return d

