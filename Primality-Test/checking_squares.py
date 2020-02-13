import math
import struct

def is_square_type1(num):
    pass


def fast_inverse_sqrt(num):
    """
    An algorithm that is fast at calculating 1/sqrt(x) 
    inverse-sqrt is required for lighting and reflections in 3d games
    I found out about this algorithm because the game "quake" implimented this for the purpose stated above

    the implimentation in quake is very confusing so I decided to break it down so I would understand
    you just need to know calculus, specifically newton's method
    newton's method: https://en.wikipedia.org/wiki/Newton%27s_method 
        f(x) is the function and you're trying to find the root
        f'[x] is the derivative
        x[i] is the i-th "guess"

        x[n+1] = x[n] + f(x[n])/f'(x[n])
        as n approaches infinity, the value of x[n] converges to a root

    check the following wiki page for more indepth analysis:
    https://en.wikipedia.org/wiki/Fast_inverse_square_root
    """
    # since the whole algorithm depends on floating point representation of numbers, namely in 32bits
    # I will use the python's standard module "struct" because it represents the value as byte objects
    
    # the smart thing that this algorithm does is that it's a method of finding inverse sqrt without doing the inverse sqrt operation
    # essentially the trick is to make the value of the inverse sqrt a root of a equation and using newton's method to find a good approximation of it
 
    # the constructed equation is the following:
    # H(x) = 1/(x^2)  - i   =  (x^-2) - i
    # the derivative:
    # H'(x) = -2 * g^-3

    # using the newton's formula we get the following:
    # ==> x[n+1] = g * (1.5 - 1/2 * i * g^2)

    #a tuple is returned even if there's one value being returned, hence the [0]
    # just converting the value from a float to an int
    i = struct.unpack("i", struct.pack("f", num))[0] 
    
    i = 0x5f3759df - (i >> 1) # quoting quake's developers, "what the f*ck?"
    
    # just converting the byte represented int into a floating point object in python
    y = struct.unpack("f", struct.pack("i", i))[0]
    
    
    halfnum = num * 0.5 # this is the initial guess that we will use and it's a pretty good guess
    # newton's method with only one guess
    return (y * (1.5 - (halfnum * y * y)) 


fast_inverse_sqrt(1000)