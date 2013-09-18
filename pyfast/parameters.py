'''
Created on Sep 16, 2013

@author: dcoss
'''


#MIN_RUNS_CUKIER75 = [0, 0, 19, 39, 71, 91, 167, 243, 315, 403,
MIN_RUNS_CUKIER75 = [0, 0, 0, 19, 39, 71, 91, 167, 243, 315, 403,
                     487, 579, 687, 907, 1019, 1223, 1367, 1655,
                     1919, 2087, 2351, 2771, 3087, 3427, 3555,
                     4091, 4467, 4795, 5679, 5763, 6507, 7103,
                     7523, 8351, 9187, 9667, 10211, 10775, 11339,
                     7467, 12891, 13739, 14743, 15743, 16975, 18275,
                     18927, 19907, 20759, 21803]

def generate_samples(mins, maxs, omegas, factor=1):
    import numpy as np

    Np = len(omegas)
    if Np != len(mins) or Np != len(mins):
        raise Exception("Mismatch between number of parameters"
                        " and number of parameter limits")

    if Np >= len(MIN_RUNS_CUKIER75):
        raise Exception("Cannot generate parameters for {0} input factors."
                        .format(Np))

    min_runs = MIN_RUNS_CUKIER75[Np]
    r = round(min_runs * factor)
    s = np.arange(1, r + 1)
    #s = (np.pi / r) * ((2 * s) - r - 1) / 2
    s = (np.pi / r) * ((2 * s) - r - 1) / 2

    # s = np.random.rand(min_runs)

    S = np.outer(s, omegas)

    S = (1 / np.pi) * np.arcsin(np.sin(S))

    # Transform first to (0, 1) then to (min, max)
    minval = S.min()
    S -= minval
    for col in xrange(Np):
        S[:, col] *= (maxs[col] - mins[col])
        S[:, col] += mins[col]

    return S
