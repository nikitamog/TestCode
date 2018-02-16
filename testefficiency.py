#!/usr/bin/python3


"""
Tests the runtime efficiency of the algorithms in problem 04.
"""
from timeit import timeit
from Group01Problem04 import recursive, closed_form, iterative_form, tail_form

def tester():
    print('Closed Form')
    print('%4s :  milliseconds' % 'val')
    print('------------------------------')
    for x in range(int(1000/50)+1):
        print('%4d : ' % (x*50), timeit('closed_form(%d)' % (x*50),
                                        'from Group01Problem04 import closed_form',
                                        number=1))

tester()