#******************************************************************************
# to understand the math and what each function is doing, refrence the wiki pages below:
#https://en.wikipedia.org/wiki/Jacobi_symbol
#https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test
#https://en.wikipedia.org/wiki/Lucas_pseudoprime

import math
import time

def baillie_PSW(n):
    """first simple check of primality, if inconclusive, go to baillie PSW test"""
    if n < 2 or not (n&1): return False
    if n == 2: return True
    if n <= 10000:# for a small n, it checks square roots
        for a in range(3, int(math.sqrt(n))+1,2): #check all odd number up to sqrt(n)
            if n%a == 0: return False
        return True
    for i in [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]: # check other small primes
        if n%i == 0 and n != i: return False
    
    # if the trivial cases above doesnt work, then it goes to the big gun
    
    "This funcion starts the primality tests, first checks Miller-Rabbin then check Lucas test. both checks must be satisfied to be a prime"
    if  miller_rabbin_test(n): #checks miller first, because the calculation is faster and removes most non-primes
        if lucas_test(n):
            return True
    return False 

def miller_rabbin_test(n):
    "this does the miller test with base 2, it breaks up n-1 into the form 2^k * d and find if 2^(2t*d) = 1 or -1, for t in the range between [0,k]"
    number, pow_of_two= n-1, 0
    while True: # convert n-1 into the form 2^k * d
        if not number & 1:
            number = number//2
            pow_of_two+=1
        else: break
    if number < 1001: base_2 = (2**number)%n   
    else: base_2 = exp_and_mod(2,number,n) #if 2^number is too big to calculate, it sends it to a function
    if abs(base_2) == 1: return True
    for t in range(pow_of_two):
        base_2 = (base_2**2)%n
        if abs(base_2) == 1: return True
    return False

def lucas_test(n):
    "starts the lucas test, first checks if n is a square number, then it will look for the first D that satisfy the jacobi symbol (k,n) = -1, then do checks for primamlity"
    if math.sqrt(n)%1 == 0: return False #check if the number is a perfect square, because lucas test will be indeterminant, if n is a square
    D_and_Q = find_D(n) # this will find a D value that makes the jacobi symbol = -1
    D, Q, P = D_and_Q[0], D_and_Q[1], 1 
    Un, Vn = recursive_UV(P,Q,D,n+1,n)# this will find U and V through a recursive function ***********************************************************************************
    if Un%n == 0:
        if Vn%n == (2*Q)%n: # needs to satisfy both conditions for n to be prime
            return True
    return False

def recursive_UV(P,Q, D, n, N):
    "recursive function that finds U and V, will end when n == 1 or 2"
    if n == 1: return [1, 1] #if n == 0: then return [1,2], but this is unnecessary for this code
    if n & 1: # if n is odd
        UVlist = recursive_UV(P,Q,D,n-1,N)# calls itself with n-1
        U, V = UVlist[0], UVlist[1]
        Uk, Vk= int(U + V), int(D*U + V)
        if Uk & 1: Uk += N
        if Vk & 1: Vk += N
        return [(Uk/2)%N, (Vk/2)%N]
    else: # if n is even
        if n == 2: return [1, (1-(2*Q))%N]
        n = n//2
        UVlist = recursive_UV(P,Q,D,n,N) # call itself with n/2
        U, V= UVlist[0], UVlist[1]
        return [(U*V)%N, (V**2 + (-2*exp_and_mod(int(Q),int(n),N)))%N]

def exp_and_mod(base,exponent,n): 
    "return (base^exponent) modulo n,  this function is used when trying to find base to the power of a huge number, then do modulo n"
    if exponent == 0: return 1
    if exponent%2 == 0: base = abs(base)
    if base == 0 or base == 1: return base
    if base == 4: base, exponent = 2, 2* exponent
    if abs(base) == 2: sub_exponent = 128 # divide and conquer strategy, split exponents so base^exponent is less or equal to 2^256 and do mod n at each iteration
    elif abs(base) == 3: sub_exponent = 80
    elif abs(base) == 5: sub_exponent = 56
    elif abs(base) <= 10: sub_exponent = 38
    elif abs(base) <= 100: sub_exponent = 9
    else: print("need to rewrite exponent and mod function")
    quotient, remainder, new_base = exponent//sub_exponent, exponent%sub_exponent, (base**sub_exponent)%n
    rest = (base**remainder)%n
    if quotient == 0:return rest
    else:
        while quotient != 1:
            if not quotient & 1: #quotient is even
                new_base, quotient = (new_base**2)%n,  quotient//2
            else: #quotient is odd
                quotient -=1
                rest = (rest*new_base)%n 
        return (new_base*rest)%n

    
def jacobi_symbol(a ,p): 
    "this is a function that returns the value of jacobi symbol (a,p), p must be prime, returns 0, 1, or -1"
    t, a = 1, a%p
    while a != 0:
        while not a & 1: #after this a is definitly odd
            j, a = p%8, a//2
            if j == 3 or j == 5: t = -t
        if a%4 == 3 and p%4 == 3: t = -t
        a, p = p, a
        a = a%p
    if p == 1: return t
    return 0

def find_D(n): 
    "finds the D value that makes the jacobi_symbol = -1, return [D, Q]"
    D = 5
    while True:
        if D> 0 and math.sqrt(D)%1 != 0: pass
        else:
            if jacobi_symbol(D, n) == -1: break
        if D > 0: D = -1*(abs(D)+2)
        else: D = (abs(D)+2)
    return [D,(1-D)/4] #return D and Q

def find_prime_in_range(a, b):
    
    if a < 0 or b < 0: 
        print("both upperbound and lower bound must be greater than zero")
        return None
    elif a > b:
        print("a must be less than b")
        return None
    else:
        if a < 3: a = 1
        if not a&1: a+=1
        current = -1
        print(a, b)
        for i in range(a, b, 2):
            if baillie_PSW(i):
                past_prime = current
                current = i
                if current-past_prime == 2:
                    yield (past_prime, current)

def main():

    t1 = time.time()
    a = 100000000
    for i in find_prime_in_range(a, a+1000000):
        #print(i)
        a = 1
    print(time.time()-t1)

if __name__ == "__main__":
    main()