# Init


class Cukier():
    def __init__(self, omega_0_list, delta_omega_list):
        self.omega_0_list = omega_0_list
        self.delta_omega_list = delta_omega_list

    def freq(self, m, i=1, omega_0=0):
        if i <= 1:
            omega = self.omega_0_list[m - 1]
            return [omega] + list(self.freq(m, i + 1, omega))

        o = omega_0 + self.delta_omega_list[m - i]

        if i == m:
            return [o]

        return [o] + self.freq(m, i + 1, o)


def get_fast_parameters(mins, maxs, omegas):
    from pyfast.parameters import generate_samples
    N = len(mins)
    
    return generate_samples(mins, maxs, omegas)
