"""
Utilities for bootstrapping statistics.
"""

import numpy as np

def draw_bs_reps(data, func, rg=np.random.default_rng(), size=1, args=()):
    """
    Draws bootstrap replicates out of a single set of repeated measurements.
    Function inputs:
    `data`: a NumPy array of data
    `func`: a function to apply to the data array that returns a statistic
    `rg`: an instance of a NumPy random number generator. Defaults to the NumPy default RNG.
    `size`: the number of replicates to generate. Defaults to 1.
    `args`: arguments to pass to `func`.
    
    Returns a NumPy array of bootstrap replicates.
    """

    
    n = len(data)
    
    return np.array([func(rg.choice(data, size=n, replace=True), *args) for _ in range(size)])
    


def draw_bs_pairs(data1, data2, func, rg=np.random.default_rng(), size=1, args=()):
    """
    Draws pairs of data points out of `data1` and `data2` and uses them to
    compute bootstrap replicates. Assumes `data1` and `data2` are the same length.
    Function inputs:
    `data`: a NumPy array of data
    `func`: a function to apply to the data array that returns a statistic
    `rg`: an instance of a NumPy random number generator. Defaults to the NumPy default RNG.
    `size`: the number of replicates to generate. Defaults to 1.
    `args`: arguments to pass to `func`.
    
    Returns a NumPy array of bootstrap pairs.
    """
    
    n = len(data1)
    
    bs_reps = np.empty(size)
    
    for i in range(size):
        ind = rg.choice(np.arange(n), size=1)
        a1, a2 = data1[ind], data2[ind]
        bs_reps[i] = func(a1, a2, *args)
        
    return bs_reps