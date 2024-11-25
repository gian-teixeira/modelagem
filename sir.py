import numpy as np
from model import Model
from plot import Plot

class SIR(Model):
    def initial_state(self):
        return np.array((10, 1, 0))
    
    @property
    def plot_data(self):
        return Plot.Data(['S', 'I', 'R'])

    @staticmethod
    def system(time, state):
        beta = 0.2
        gamma = 0.2

        S, I, R = state

        return np.array((
            -beta * I * S,
            beta * I * S - gamma * I,
            gamma * I
        ))

if __name__ == '__main__':
    model = SIR()
    tmp = model.evaluate(50)
    Plot.plot(tmp, model.plot_data)
    print(tmp)
