import numpy as np

class Recipe():
    def __init__(self):
        self.ingredients = []
        self.mix_methods = []

    def add_ingredient(self, ingredient, mix_method):
        self.ingredients.append(ingredient)
        self.mix_methods.append(mix_method)

    def cook_recipe(self, grid, seed=None):
        """"Cooks up a recipe."""
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
        for idx, ing in enumerate(self.ingredients[1:]) :
            # evaluate the ingredient on the grid
            y = ing.eval(grid)
            ings_evaluated[idx+1,:] = y

            # mix the ingredient into the dish
            cumulative[idx+1] = cumulative[idx] + y
            
        return cumulative[-1], ings_evaluated, cumulative