import matplotlib.pyplot as plt
import warnings

class Ingredient():
    """Functional representation of data (signal or noise) to be created

    Attributes:
        func (:obj:`function`): Functional representation of data to be created
        label (:obj:`str`): Name or short description of ingredient 

    """


    def __init__(self, func, label, **kwargs):
        """Ingredient constructor
        
        Create an ingredient object containing a function representation, 
        other necessary arguments, and a descriptive label

        Args:
            func (:obj:`function`): Function representation of ingredient
            label (:obj:`str`): Name or short description of ingredient to help 
                identify distinguish amongst other ingredients
        """
        self.func = func
        self.kwargs = kwargs
        self.label = label

    def plot(self, x):
        """Evaluate and plot ingredient
        
        Evaluate the ingredient function at specified point(s) and plot
        result of evaluation versus respective point(s)

        Args:
            x (:obj:`array`): numpy array or list of floats or ints. Grid on which to 
                evaluate the ingredient function and plot against.
        """
        plt.plot(x, self.eval(x), marker='.', c='k')
        plt.title(f"Ingredient '{self.label}'")
    
    def eval(self, x):
        """Evaluate ingredient
        
        Evaluate the ingredient function at specified point(s) 

        Args:
            x (:obj:`array`): numpy array or list of floats or ints. Grid on which to 
                evaluate the ingredient function.
        """
        if len(x) == 0:
            print("Cannot eval on empty array")
            return None
        return self.func(x, **self.kwargs)