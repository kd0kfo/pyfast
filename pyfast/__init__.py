# Init

CUKIER_FREQUENCIES = [0, 0, 1, 5, 11, 1, 17, 23, 19, 25, 41, 31, 23,
                      87, 67, 73, 58, 143, 149, 99, 119, 237, 267, 283,
                      151, 385, 157, 215, 449, 163, 337, 253, 375, 441,
                      673, 773, 875, 873, 587, 849, 623, 637, 891, 943,
                      1171, 1225, 1335, 1725, 1663, 2019]

CUKIER_FREQ_OFFSETS = [4, 8, 6, 10, 20, 22, 32, 40, 38, 26, 56, 62, 46,
                       76, 96, 60, 86, 126, 134, 112, 92, 128, 154, 196,
                       34, 416, 106, 208, 328, 198, 382, 88, 348, 186, 140,
                       170, 284, 568, 302, 438, 410, 248, 448, 388, 596, 217,
                       100, 488, 166]


def freq(m, i=1, omega_0=0, omega_0_list=CUKIER_FREQUENCIES,
         delta_omega_list=CUKIER_FREQ_OFFSETS):
    if i <= 1:
        omega = omega_0_list[m - 1]
        return [omega] + list(freq(m, i + 1, omega))

    o = omega_0 + delta_omega_list[m - i]

    if i == m:
        return [o]

    return [o] + freq(m, i + 1, o)


def get_fast_parameters(mins, maxs, omegas):
    from pyfast.parameters import generate_samples
    
    return generate_samples(mins, maxs, omegas)


def double_series(x):
    if not x:
        return x

    return x.reverse()[1:]

def fast(model, num_params, M=4):
    from pyfast.parameters import MIN_RUNS_CUKIER75
    import numpy as np

    nsamples = len(model)

    # TODO: Add model dimension checks

    FF = np.abs(np.fft(double_series(model))) / nsamples
    FF = FF[:nsamples]

    # Frequencies
    cukier = freq(num_params)
    frequencies = np.outer(cukier, np.arange(1, M + 1))

    # Sensitivity Values
    total = np.sum(FF[1:] ** 2)
    sensitivities = []
    for i in xrange(0, frequencies.shape[0]):
        frequency_vals = FF[frequencies[i, :] + 1]
        sensitivities.append(np.sum(frequency_vals ** 2) / total)

    return sensitivities
