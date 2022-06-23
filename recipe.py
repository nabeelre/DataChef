import numpy as np
import matplotlib.pyplot as plt

class Recipe():
    """A list of steps to cook up a simulated data set.

    A Recipe stores a list of Ingredients and the method by which they will be mixed
    in to generate a simulated data set. 

    Attributes:
        ingredients (`list`): lists of Ingredients in the Recipe, in order of application
        mix_funcs (`list`): lists the mixing functions by which Ingredients will be added, in order of application
        label (`str`): the name of the Recipe


    """
    def __init__(self, label="recipe"):
        """Initialize a Recipe object.

        Recipes store a list of Ingredients and the methods that they will be mixed
        into the dataset. Use 

        Args:
            label (:obj:`str`, optional) : the name of the Recipe
        """ 
        self.ingredients = []
        self.mix_funcs = []
        # self.eval = self.cook_recipe
        self.label = label

    def print(self):
        """Print a summary of the Recipe."""
        print('Recipe Summary')

        for idx, (ing, mix) in enumerate(zip(self.ingredients, self.mix_funcs)):
            print(str(idx) + ': ' + ing.label + ', ' + mix.__name__)

    def add_ingredient(self, ingredient, mix_func):
        """Add an Ingredient object to a Recipe.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            ingredient (`Ingredient object`): The Ingredient object to be added
            mix_func(`function`): A function that takes in two arrays of equal length, mixes them in some way into a 1D array and returns it

        """
        # TO DO: Make it possible to insert an ingredient by index into the middle of Recipe
        self.ingredients.append(ingredient)
        self.mix_funcs.append(mix_func)

    def add_recipe(self, recipe):
        """Adds one Recipe line by line into this one.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            recipe (`Recipe object`): The Recipe object to be added

        """
        # TO DO: Update (talk to Rae)
        for idx, (ing, mix) in enumerate(zip(recipe.ingredients, recipe.mix_funcs)) :
            self.ingredients.append(ing)
            self.mix_funcs.append(mix)            

    def plot(self, grid, seed=None):
        final, _, _ = Recipe.cook_recipe(self, grid, seed)
        plt.plot(grid, final, marker='.', c='k')
        ing_labels = ""
        for ing in self.ingredients:
            ing_labels += ing.label + ", "
        ing_labels = ing_labels[0:-2]
        plt.title(f"Ingredients: {ing_labels}")

    def cook_recipe(self, grid, seed=None, export_eval=None, export_cum=None):
        """"Cooks up a recipe."""
        # TO DO: Make compatible with grids of higher dimention

        if seed is not None:
            np.random.seed(seed)

        # array to store the y array for each ingredient evaluated over the grid
        ings_evaluated = np.zeros((len(self.ingredients),len(grid)))
        # array to store the state of the "base" after each ingredient is added
        cumulative = np.zeros((len(self.ingredients),len(grid)))

        # add in the first ingredient
        ings_evaluated[0] = self.ingredients[0].eval(grid)
        cumulative[0] = self.ingredients[0].eval(grid)
        
        # loop through the ingredients and add them in
        for idx, (ing, mix) in enumerate(zip(self.ingredients[1:], self.mix_funcs[1:])) :
            # evaluate the ingredient on the grid
            y = ing.eval(grid)
            ings_evaluated[idx+1,:] = y

            # mix the ingredient into the dish
            cumulative[idx+1] = mix(cumulative[idx],y)

        # export the evaluated ingredient to csv
        if export_eval is not None:
            np.savetxt(fname=export_eval, X=y)
        if export_cum is not None:
            np.savetxt(fname=export_cum, X=cumulative)
            
        return cumulative[-1], ings_evaluated, cumulative