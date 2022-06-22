class Ingredient():
    def __init__(self, func, label, is_signal=False, **kwargs):

        # Instantiation differs depending on the input type to func

        # If func is a string, look up the built in function in the ingredient dictionary

        # If func is a 
        self.func = func
        self.kwargs = kwargs
        self.is_signal = is_signal
        self.label = label
    
    def test(self, x):
        """For testing outputs"""
        print(self.label)
        print(self.eval(x))
    
    def eval(self, x):
        return self.func(x, **self.kwargs)