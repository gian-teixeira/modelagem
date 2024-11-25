import numpy as np
from model import Model
from plot import Plot

class ImmuneSimple(Model):
    def initial_state(self):
        return np.array((10, 1, 0))
    
    @property
    def plot_data(self):
        return Plot.Data(['TD', 'N', 'CH'])

    @staticmethod
    def system(time, state):
        alpha = 0.2
        beta = 0.2
        gamma = 0.2
        delta = 0.2

        TD, N, CH = state

        return np.array((
            alpha * N,
            beta * TD + gamma * CH - alpha * N,
            gamma * N - delta * CH
        ))

class ImmuneComplete(Model):
    def initial_state(self):
        return np.array((10, 0, 5, 0, 0))

    @property
    def plot_data(self):
        return Plot.Data(['TD', 'N', 'CH', 'MREG', 'AC'])

    @staticmethod
    def system(time, state):
        alpha = 0.6
        beta = 0.2
        gamma = 0.2
        delta = 0.2
        epsilon = 0.5
        zeta = 0.2
        eta = 0.3
        theta = 0.2
        iota = 0.2
        kappa = 0.2

        TD, N, CH, MREG, AC = state

        return np.array((
            alpha * N - epsilon * MREG,
            beta * TD + gamma * CH / (1 + kappa * AC) - alpha * N,
            gamma * N / (1 + kappa * AC) - delta * CH,
            zeta * N - eta * MREG,
            theta * MREG - iota * AC
        ))

if __name__ == '__main__':
    model = ImmuneComplete()
    tmp = model.evaluate(50)
    Plot.plot(tmp, model.plot_data)
    print(tmp)
