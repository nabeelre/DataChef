import numpy as np

def line(x, m=1, b=0):
    '''Function to make a straight line with slope m and intercept b.

    Args:
        x (array): numpy vector. grid to make line on.
        m (int or float, optional): slope of the line.
                                    default is 1.
        b (int or float, optional): intercept of the line.
                                    default is 0.

    Returns:
        array: m*x + b.
    '''
    return x*m+b
    
def parabola(x, a=1, b=0, c=0):
    '''Function to make a parabola.

    Args:
        x (array): numpy vector. grid to make parabola on.
        a (int or float, optional): second order coefficient. default is 1.
        b (int or float, optional): first order coefficient. default is 0.
        c (int or float, optional): zeroth order coefficient. default is 0.

    Returns:
        array: a*x**2 + b*x + c.
    '''
    return a*x**2 + b*x + c

def cubic(x, a=1, b=0, c=0, d=0):
    '''Function to make a cubic.

    Args:
        x (array): numpy vector. grid to make cubic on.
        a (int or float, optional): third order coefficient. default is 1.
        b (int or float, optional): second order coefficient. default is 0.
        c (int or float, optional): first order coefficient. default is 0.
        d (int or float, optional): zeroth order coefficient. default is 0.

    Returns:
        array: a*x**3 + b*x**2 + c*x + d.
    '''

    return a*x**3 + b*x**2 + c*x + d

def sinusoid(x, phase=0, amplitude=1, period=2*np.pi):
    '''Function to make a sinusoid.

    Args:
        x (array): numpy vector. grid to make sinusoid on.
        phase (int or float, optional): initial phase of the sinusoid. default is 0.
        amplitude (int or float, optional): amplitude of the sinusoid. default is 1.
        period (int or float, optional): period of the sinusoid. default is 2*pi.

    Returns:
        array: A * sin(Bx + C), where A is the amplitude, B is 2*pi / period, C is the initial phase.
    '''

    return amplitude*np.sin(2*np.pi / period*x + phase)

def uniform(x, shift=0, scale=1):
    '''Function to generate random white noise.

    Args:
        x (array): numpy vector. grid to make white noise on.
        shift (int or float, optional): shift to the uniform distribution. default is 0.
        scale (int or float, optional): scale to the uniform distribution. default is 1.

    Returns:
        array: uniform distribution.
    '''

    return scale * np.random.rand(len(x)) + shift

def gaussian(x, mean=0, stdev=1):
    '''Function to generate random gaussian noise.

    Args:
        x (array): numpy vector. grid to make gaussian noise on.
        mean (int or float, optional): mean of the Gaussian distribution. default is 0.
        stdev (int or float, optional): standard deviation to the Gaussian distribution. default is 1.

    Returns:
        array: Gaussian distribution.
    '''
    return np.random.normal(loc=mean, scale=stdev, size=x)

def poisson(x, lam=0):
    '''Function to generate random Poisson noise.

    Args:
        x (array): numpy vector. grid to make white noise on.
        lam (int or float, optional): expectation of interval, must be >= 0.

    Returns:
        array: Poisson distribution.
    '''

    return np.random.poisson(lam=lam, size=x)