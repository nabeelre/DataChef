#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from recipe import Recipe
from ingredient import Ingredient
import ingredient_functions as ing_funcs
import mix_functions as mix_funcs

if __name__ == "__main__":
    # make some ingredients for testing
    ing  = Ingredient(ing_funcs.line, "line", is_signal=True, m=10, b=1)
    ing2 = Ingredient(ing_funcs.line, "line", is_signal=True, m=-5, b=1)
    ing3 = Ingredient(ing_funcs.white_noise, "white noise", is_signal=False, scale=1.5, shift=2)

    # Run test function on an ingredient
    # ing.test(np.linspace(0,10,11))

    # ingredients that use a custom function
    # def custom(x, a, b, c):
    #     print(a,b,c)
    #     return a*x + b + c
    # ing_cust = Ingredient(custom, "custom", a=1, b=2, c=3)
    # ing_cust.test(np.linspace(0,10,11))

    # ingsin = Ingredient(np.sin, 'sin', False)
    # ingsin.test(np.linspace(-1,1,11))

    # add ingredients to the Recipe
    recipe = Recipe()
    recipe.add_ingredient(ing , mix_funcs.add)
    recipe.add_ingredient(ing2, mix_funcs.add)
    recipe.add_ingredient(ing3, mix_funcs.add)

    # Cook the recipe
    x = np.linspace(-1,1,11)
    y, ing_eval, ing_comp = recipe.cook_recipe(x, export_eval='./test_export/first_eval_test.csv', 
                                                    export_cum='./test_export/first_cum_test.csv')

    # plot results
    plt.plot(x,y)
    plt.show()

    # plot each indiviual ingredient
    for i in range(len(recipe.ingredients)):
        plt.plot(x, ing_eval[i])
        plt.show()


