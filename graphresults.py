#!/usr/bin/python3

"""
Graphs a representation of the effeciency data.

"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import seaborn as sns
import pylab
from timeit import timeit

np.random.seed(sum(map(ord, "aesthetics")))

"""
# can handle 1000 just fine.
x = np.linspace(0, 1000, int(1000/50)+1, dtype=int)
closedvals = []
for i in range(int(1000/50)+1):
    closedvals.append(timeit('closed_form(%d)' % (i*50),
                           'from Group01Problem04 import closed_form',
                           number=1))
"""
"""
# probably can't handle more than 25
maxval = 30
delta = 5
iterint = int(maxval/delta)
x = np.linspace(0, maxval, iterint+1, dtype=int)
recursivevals = []
for i in range(iterint+1):
    recursivevals.append(timeit('recursive(%d)' % (i*delta),
                           'from Group01Problem04 import recursive',
                           number=1))
"""

"""
# maybe 300?
maxval = 50
delta = 5
iterint = int(maxval/delta)
x = np.linspace(0, maxval, iterint+1, dtype=int)
itervals = []
for i in range(iterint+1):
    itervals.append(timeit('iterative_form(%d)' % (i*delta),
                           'from Group01Problem04 import iterative_form',
                           number=1))
"""

# seems linear. Go ham.
maxval = 50
delta = 5
iterint = int(maxval/delta)
x = np.linspace(0, maxval, iterint+1, dtype=int)
tailvals = []
for i in range(iterint+1):
    tailvals.append(timeit('tail_form(%d)' % (i*delta),
                           'from Group01Problem04 import tail_form',
                           number=1))



def sinplot():
    plt.plot(x, tailvals, 'bo')

ax = plt.axes()
ax.set_title('Tail Form Runtime Performance')
ax.yaxis.set_major_formatter(FormatStrFormatter('%g'))
plt.ylabel('Runtime (s)')
plt.xlabel('Parameter Values')
sns.set()
sinplot()            
pylab.show()