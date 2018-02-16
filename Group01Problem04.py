#!/usr/bin/python3

"""

Math 301

given base cases of a(0) = 3, a(1) = -5, a(2) = 29/2
1. Solving the recurrence relation
   a(n) = 1/2(a(n-1)) + 7/2(a(n-2)) - 3(a(n-3))
2. produces the factored form (assuming the shift function S for a(n-3))
   1/2(s-1)(s+2)(2s-3) = 0
3. the roots for this equation are
   s = 1, -2, 3/2
4. A = -2, B = 3, C = 2

"""

def recursive(n):
    """ 
    Assumes integer inputs
    Runs the functions resursively.
    """
    if(n == 0): # run the base cases first.
        return 3
    elif(n == 1):
        return -5
    elif(n == 2):
        return 29/2
    else:
        return (1/2)*recursive(n-1) + (7/2)*recursive(n-2) - 3*recursive(n-3)

def closed_form(n):
    """ 
    Assumes integer inputs
    Generates the value using a closed-form function
    """
    return -2*1**n + 3*(-2)**n + 2*(3/2)**n

def iterative_form(n, n_minus1=(29/2), n_minus2=(-5), n_minus3=(3)):
    """
    Assumes integer inputs.
    """
    while(n >= 1):
        (n, n_minus1, n_minus2, n_minus3) = (n-1, (1/2)*n_minus1 + (7/2)*n_minus2 - 3*n_minus3,
                                             n_minus1, n_minus2)
    return n_minus1

def tail_form(n, n_minus1=(29/2), n_minus2=(-5), n_minus3=(3)):
    """
    Assumes integer inputs
    """
    if n <= 1:
        return n_minus1
    else:
        return tail_form(n-1, (1/2)*n_minus1 + (7/2)*n_minus2 - 3*n_minus3,
                         n_minus1, n_minus2)
