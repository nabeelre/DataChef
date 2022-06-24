import numpy as np
from uncertainties import unumpy


def line(x, m=1, b=0):
    '''Function to make a straight line with slope m and intercept b.

    Args:
        x (:obj:`array`): numpy vector. grid to make line on.
        m (:obj:`int` or :obj:`float`, optional): slope of the line. Default is 1.
        b (:obj:`int` or :obj:`float`, optional): intercept of the line. Default is 0.

    Returns:
        :obj:`array`: m*x + b.
    '''
    return x*m+b
    
def parabola(x, a=1, b=0, c=0):
    '''Function to make a parabola.

    Args:
        x (:obj:`array`): numpy vector. grid to make parabola on.
        a (:obj:`int` or :obj:`float`, optional): second order coefficient. Default is 1.
        b (:obj:`int` or :obj:`float`, optional): first order coefficient. Default is 0.
        c (:obj:`int` or :obj:`float`, optional): zeroth order coefficient. Default is 0.

    Returns:
        :obj:`array`: a*x**2 + b*x + c.
    '''
    return a*x**2 + b*x + c

def cubic(x, a=1, b=0, c=0, d=0):
    '''Function to make a cubic.

    Args:
        x (:obj:`array`): numpy vector. grid to make cubic on.
        a (:obj:`int` or :obj:`float`, optional): third order coefficient. 
        b (:obj:`int` or :obj:`float`, optional): second order coefficient. Default is 1.
        c (:obj:`int` or :obj:`float`, optional): first order coefficient. Default is 0.
        d (:obj:`int` or :obj:`float`, optional): zeroth order coefficient. Default is 0.

    Returns:
        :obj:`array`: a*x**3 + b*x**2 + c*x + d.
    '''

    return a*x**3 + b*x**2 + c*x + d

def sinusoid(x, phase=0, amplitude=1, period=2*np.pi):
    '''Function to make a sinusoid.

    Args:
        x (:obj:`array`): numpy vector. grid to make cubic on.
        phase (:obj:`int` or :obj:`float`, optional): third order coefficient. Default is 0.
        amplitude (:obj:`int` or :obj:`float`, optional): second order coefficient. Default is 1.
        period (:obj:`int` or :obj:`float`, optional): first order coefficient. Default is 2*pi.

    Returns:
        :obj:`array`: A * sin(Bx + C), where A is the amplitude, B is 2*pi / period, C is the initial phase.
    '''

    return amplitude*np.sin(2*np.pi / period*x + phase)

def uniform(x, shift=0, scale=1):
    '''Function to generate random white noise.

    Args:
        x (:obj:`array`): numpy vector. grid to make white noise on.
        shift (:obj:`int` or :obj:`float`, optional): shift to the uniform distribution. Default is 0.
        scale (:obj:`int` or :obj:`float`, optional): scale to the uniform distribution. Default is 1.

    Returns:
        :obj:`array`: uniform distribution.
    '''

    return scale * np.random.rand(len(x)) + shift

def gaussian(x, mean=0, stdev=1):
    '''Function to generate random gaussian noise.

    Args:
        x (:obj:`array`): numpy vector. grid to make gaussian noise on.
        mean (:obj:`int` or :obj:`float`, optional): mean of the Gaussian distribution. Default is 0.
        stdev (:obj:`int` or :obj:`float`, optional): standard deviation to the Gaussian distribution. Default is 1.

    Returns:
        :obj:`array`: Gaussian distribution.
    '''
    return np.random.normal(loc=mean, scale=stdev, size=x)

def poisson(x, lam=0):
    '''Function to generate random Poisson noise.

    Args:
        x (:obj:`array`): numpy vector. grid to make white noise on.
        lam (:obj:`int` or :obj:`float`, optional): expectation of interval, must be >= 0.

    Returns:
        :obj:`array`: Poisson distribution.
    '''

    return np.random.poisson(lam=lam, size=x)