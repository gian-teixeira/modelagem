from abc import ABC, abstractmethod
from scipy.integrate import solve_ivp

class Model(ABC):
    @abstractmethod
    def initial_state(self): ...

    @staticmethod
    @abstractmethod
    def system(self, time, state): ...

    @property 
    @abstractmethod
    def plot_data(self): ...

    def evaluate(self, tmax):
        return solve_ivp(self.system, [0,tmax], self.initial_state())

