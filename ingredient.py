import matplotlib.pyplot as plt

class Ingredient():
    def __init__(self, func, label, is_signal=False, **kwargs):
        self.func = func
        self.kwargs = kwargs
        self.is_signal = is_signal
        self.label = label

    def plot(self, x):
        plt.plot(x, self.eval(x), marker='.', c='k')
        plt.title(f"Ingredient '{self.label}'")
    
    def eval(self, x):
        """Evaluates the functional form of the ingredient on an array of x values."""
        return self.func(x, **self.kwargs)