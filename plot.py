from dataclasses import dataclass
import matplotlib.pyplot as plt

class Plot():
    @dataclass
    class Data():
        curve_names : list[str]

    @staticmethod
    def plot(result, plot_data):
        figure, axis = plt.subplots()
        for curve,name in zip(result.y, plot_data.curve_names):
            axis.plot(result.t, curve, label = name)
        plt.legend()
        plt.show()

