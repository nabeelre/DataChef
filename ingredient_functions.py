import numpy as np

def line(x, m=1, b=0):
    '''Function to make a straight line with slope m and intercept b.

    Args:
        x (:obj:`array`): numpy vector. grid to make line on.
        m (:obj:`int` or :obj:`float`, optional): slope of the line.
        b (:obj:`int` or :obj:`float`, optional): intercept of the line.

    Returns:
        array: m*x + b.
    '''
    return x*m+b
    
def parabola(x, a=1, b=0, c=0):
    '''Function to make a parabola.

    Args:
        x (:obj:`array`): numpy vector. grid to make parabola on.
        a (:obj:`int` or :obj:`float`): second order coefficient.
        b (:obj:`int` or :obj:`float`): first order coefficient.
        c (:obj:`int` or :obj:`float`): zeroth order coefficient.

    Returns:
        array: a*x**2 + b*x + c.
    '''
    return a*x**2 + b*x + c

def cubic(x, a=1, b=0, c=0, d=0):
    '''Function to make a cubic.

    Args:
        x (:obj:`array`): numpy vector. grid to make cubic on.
        a (:obj:`int` or :obj:`float`): third order coefficient.
        b (:obj:`int` or :obj:`float`): second order coefficient.
        c (:obj:`int` or :obj:`float`): first order coefficient.
        d (:obj:`int` or :obj:`float`): zeroth order coefficient.

    Returns:
        array: a*x**3 + b*x**2 + c*x + d.
    '''

    return a*x**3 + b*x**2 + c*x + d

def sinusoid(x, phase=0, amplitude=1, period=2*np.pi):
    '''Function to make a sinusoid.

    Args:
        x (:obj:`array`): numpy vector. grid to make cubic on.
        phase (:obj:`int` or :obj:`float`): third order coefficient.
        amplitude (:obj:`int` or :obj:`float`): second order coefficient.
        period (:obj:`int` or :obj:`float`): first order coefficient.

    Returns:
        :obj:`array`: a*x**3 + b*x**2 + c*x + d.
    '''

    return amplitude*np.sin(period*x+phase)

def uniform(x, shift=0, scale=1):
    return scale * np.random.rand(len(x)) + shift

def gaussian(x, mean, stdev):
    return np.random.normal(loc=mean, scale=stdev, size=x)

def poisson(x, lam):


    return np.random.poisson(lam=lam, size=x)