import numpy as np

def line(x, m=1, b=0):
    return x*m+b

def parabola(x, a=1, b=1, c=1):
    return a*x**2 + b*x + c

def white_noise(x, shift=0, scale=1):
    return scale * np.random.rand(len(x)) + shift