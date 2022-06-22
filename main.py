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

    ing = Ingredient(line, "line", True, m=10, b=1)
    ing2 = Ingredient(line, "line", True, m=-10, b=1)

    ing.test(np.linspace(0,10,11))

    ing_cust = Ingredient(custom, "custom", a=1, b=2, c=3)
    ing_cust.test(np.linspace(0,10,11))

    ingsin = Ingredient(np.sin, 'sin', False)
    ingsin.test(np.linspace(-1,1,11))

    recipe = Recipe()
    recipe.add_ingredient(ing, "empty")
    recipe.add_ingredient(ing2, 'empty')

    x = np.linspace(-1,1,11)
    y = recipe.cook_recipe(x)

    plt.plot(x,y)
    plt.show()
