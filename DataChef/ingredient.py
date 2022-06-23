import matplotlib.pyplot as plt
from uncertainties import unumpy


class Ingredient():
    """Functional representation of data (signal or noise) to be created

    Attributes:
        func (:obj:`function`): Functional representation of data to be created
        label (:obj:`str`): Name or short description of ingredient 

    """


    def __init__(self, func, label, error_func=None, **kwargs):
        """Ingredient constructor
        
        Create an ingredient object containing a function representation, 
        other necessary arguments, and a descriptive label

        Args:
            func (:obj:`function`): Function representation of ingredient
            label (:obj:`str`): Name or short description of ingredient to help 
                identify distinguish amongst other ingredients
            error_func (:obj:`function`): function that generates an array of error values 
                if given an x array 
        """
        self.func = func
        self.kwargs = kwargs
        self.label = label
        self.error_func = error_func
        # self.error_kwargs = error_kwargs

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
    
    def eval(self, x, yerr=None, ignore_errors=False):
        """Evaluate ingredient
        
        Evaluate the ingredient function at specified point(s) 

        Args:
            x (:obj:`array`): numpy array or list of floats or ints. Grid on which to 
                evaluate the ingredient function.
            yerr (:obj:`array`, optional): numpy array or list of floats or ints, representing  
                the error bar at each point in the `x` grid. Overrides the err_func. Must have
                the same dimensions as `x`.
            ignore_errors (:obj:`bool`, optional): if True, will evaluate without y errors  
        """
        y = self.func(x, **self.kwargs)

        if ignore_errors:
            return y

        # Apply y errors if they are provided, or if an error generating function is provided
        if yerr is not None:
            y = unumpy.uarray(y, yerr)
        elif callable(self.error_func):
            yerr = self.error_func(**self.kwargs)
            y = unumpy.uarray(y, yerr) 

        return y

    def generate_errors(self, x, error_func):
        """Generates y errors.
        
        Evaluate the ingredient function at specified point(s) 

        Args:
            x (:obj:`array`): numpy array or list of floats or ints. Grid on which to 
                evaluate the ingredient function.
            error_func (:obj:`function`): function that generates an array of error values 
                if given an x array 
        """
        return error_func(x, **self.error_kwargs)