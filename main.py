#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from recipe import Recipe
from ingredient import Ingredient

#### INGREDIENT FUNCTIONS ####

def line(x, m=1, b=0):
    return x*m+b

def parabola(x, a=1, b=1, c=1):
    return a*x**2 + b*x + c

if __name__ == "__main__":
    def custom(x, a, b, c):
        print(a,b,c)
        return a*x + b + c

    def noise(x):
        return np.random.rand(len(x))

    # make some ingredients for testing
    ing = Ingredient(line, "line", is_signal=True, m=10, b=1)
    ing2 = Ingredient(line, "line", is_signal=True, m=-10, b=1)
    ing3 = Ingredient(noise, "noise", is_signal = False)

    # Run test function on an ingredient
    ing.test(np.linspace(0,10,11))

    # ingredients that use a custom function
    # ing_cust = Ingredient(custom, "custom", a=1, b=2, c=3)
    # ing_cust.test(np.linspace(0,10,11))

    # ingsin = Ingredient(np.sin, 'sin', False)
    # ingsin.test(np.linspace(-1,1,11))

    # add ingredients to the Recipe
    recipe = Recipe(seed=3)
    recipe.add_ingredient(ing, "empty")
    recipe.add_ingredient(ing2, 'empty')
    recipe.add_ingredient(ing3, "empty")

    # Cook the recipe
    x = np.linspace(-1,1,11)
    y, ing_eval, ing_comp = recipe.cook_recipe(x)

    # plot results
    plt.plot(x,y)
    plt.show()

    # plot each indiviual ingredient
    for i in range(len(recipe.ingredients)):
        plt.plot(x, ing_eval[i])
        plt.show()


