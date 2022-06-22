class Ingredient():
    def __init__(self, func, label, is_signal=False, **kwargs):
        self.func = func
        self.kwargs = kwargs
        self.is_signal = is_signal
        self.label = label
    
    def test(self, x):
        """For testing outputs"""
        print(self.label)
        print(self.eval(x))
    
    def eval(self, x):
        """Evaluates the functional form of the ingredient on an array of x values."""
        return self.func(x, **self.kwargs)