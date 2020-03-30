import math
import struct

def is_square1(num):
    if int(math.sqrt(num) + 0.5)**2 == num:
        return True
    return False

def is_square2(num):
    # from stackoverflow
    if num==0: return True
    while num&3 == 0:    
        num=num>>2
    ## Simple bit-logic test. All perfect squares, in binary,
    ## end in 001, when powers of 4 are factored out.
    if num&7 != 1: return False
    if num==1: return True  ## is power of 4, or even power of 2

    ## Simple modulo equivalency test
    c = num%10
    if c in {3, 7}: return False  ## Not 1,4,5,6,9 in mod 10
    if num % 7 in {3, 5, 6}: return False  ## Not 1,2,4 mod 7
    if num % 9 in {2,3,5,6,8}: return False  
    if num % 13 in {2,5,6,7,8,11}: return False  

    if c == 5: # if it ends in a 5
        if (num//10)%10 != 2: return False # then it must end in 25
        if (num//100)%10 not in {0,2,6}: return False # and in 025, 225, or 625
        if (num//100)%10 == 6:
            if (num//1000)%10 not in {0,5}:
                return False    ## that is, 0625 or 5625
    else:
        if (num//10)%4 != 0: return False # (4k)*10 + (1,9)

    ## Babylonian Algorithm. Finding the integer square root.
    s = (len(str(num))-1) // 2
    x = (10**s) * 4
    A = {x, num}
    while x * x != num:
        x = (x + (num // x)) >> 1
        if x in A:
            return False
        A.add(x)
    return True

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
    return (y * (1.5 - (halfnum * y * y)))


num = 135235598**2
print(is_square2(num))