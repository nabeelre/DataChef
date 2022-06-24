import pytest
import numpy as np

from DataChef import ingredient_functions as ing_funcs
from DataChef.ingredient import Ingredient


def test_line_eval():
    """
    Check the eval function on a simple line. Tests with input as list and array
    """
    ing = Ingredient(ing_funcs.line, "line", m=10, b=-1)

    x = np.linspace(-3,6,4)
    y = ing.eval(x)
    assert [-31, -1, 29, 59] == pytest.approx(y)

    y = ing.eval(list(x))
    assert [-31, -1, 29, 59] == pytest.approx(y)

def test_parab_eval():
    """
    Check the eval function on a simple parabola. Tests with input as list and array
    """
    ing = Ingredient(ing_funcs.parabola, "line", a=1, b=0, c=0)

    x = np.array((-3,6,4))
    y = ing.eval(x)
    assert [9, 36, 16] == pytest.approx(y)

    y = ing.eval(list(x))
    assert [9, 36, 16] == pytest.approx(y)

def test_cubic_eval():
    """
    Check the eval function on a simple parabola. Tests with input as list and array
    """
    ing = Ingredient(ing_funcs.cubic, "line", a=1, b=0, c=0, d=0)

    x = np.array((-1,0,4))
    y = ing.eval(x)
    assert [-1, 0, 64] == pytest.approx(y)

    y = ing.eval(list(x))
    assert [-1, 0, 64] == pytest.approx(y)

def test_sin_eval():
    """
    Check the eval function on a simple parabola. Tests with input as list and array
    """
    ing = Ingredient(ing_funcs.sinusoid, "line", phase=0, amplitude=2, period=np.pi)

    x = np.array((-3*np.pi,0,np.pi/4))
    y = ing.eval(x)
    assert [0, 0, 2] == pytest.approx(y)

    y = ing.eval(list(x))
    assert [0, 0, 2] == pytest.approx(y)

def test_rand_seed():
    """
    Check that np.random.seed is correctly applied when specifiying a seed
    """
    x = np.linspace(-1,100,13)

    assert np.all(ing_funcs.uniform(x, seed=3) == ing_funcs.uniform(x, seed=3))

def test_empty_x():
    """
    Test the behavior of the eval funchent when given an empty x grid.
    """
    ing = Ingredient(ing_funcs.parabola, "para", a=10, b=-1, c=41)

    assert ing.eval([]) is None
    assert ing.eval(np.asarray([])) is None


test_line_eval()
test_parab_eval()
test_cubic_eval()
test_empty_x()
test_rand_seed()