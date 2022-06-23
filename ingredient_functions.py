import numpy as np

def line(x, m=1, b=0):
    '''Function to make a straight line with slope m and intercept b.

    Args:
        x (array): numpy vector. grid to make line on.
        m (int or float, optional): slope of the line.
        b (int or float, optional): intercept of the line.

    Returns:
        array: m*x + b.
    '''
    return x*m+b
    
def parabola(x, a=1, b=0, c=0):
    '''Function to make a parabola.

    Args:
        x (array): numpy vector. grid to make parabola on.
        a (int or float): second order coefficient.
        b (int or float): first order coefficient.
        c (int or float): zeroth order coefficient.

    Returns:
        array: a*x**2 + b*x + c.
    '''
    return a*x**2 + b*x + c

def cubic(x, a=1, b=0, c=0, d=0):
    '''Function to make a cubic.

    Args:
        x (array): numpy vector. grid to make cubic on.
        a (int or float): third order coefficient.
        b (int or float): second order coefficient.
        c (int or float): first order coefficient.
        d (int or float): zeroth order coefficient.

    Returns:
        array: a*x**3 + b*x**2 + c*x + d.
    '''

    return a*x**3 + b*x**2 + c*x + d

def sinusoid(x, phase=0, amplitude=1, period=2*np.pi):
    '''Function to make a sinusoid.

    Args:
        x (array): numpy vector. grid to make cubic on.
        phase (int or float): third order coefficient.
        amplitude (int or float): second order coefficient.
        period (int or float): first order coefficient.

    Returns:
        array: a*x**3 + b*x**2 + c*x + d.
    '''

    return amplitude*np.sin(period*x+phase)

def uniform(x, shift=0, scale=1):
    return scale * np.random.rand(len(x)) + shift

def gaussian(x, mean, stdev):
    return np.random.normal(loc=mean, scale=stdev, size=x)

def poisson(x, lam):


    return np.random.poisson(lam=lam, size=x)