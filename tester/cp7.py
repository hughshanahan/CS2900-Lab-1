test = {
    'name': 'checkpoint-7',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Hmm, can't find the calcCosFreqVec function. Check the name.
                    >>> # Have you defined it exactly as 'def calcCosFreqVec(f1,f2)'?
                    >>> "calcCosFreqVec" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your function does not return anything!
                    >>> # Make sure you put a return statement at the bottom of the function.
                    >>> calcCosFreqVec(f1,f2) == None
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # Your function does not return a floating point number!
                    >>> # Make sure you put a return statement at the bottom of the function.
                    >>> c = calcCosFreqVec(f1,f2)
                    >>> type(c).__name__ in ['float', 'float64']
                    True
                    """
                },

                {
                    'code': r"""
                    >>> # Your cosine calculation is wrong by at least 0.001.
                    >>> # Check if it is following the calculation described in this notebook.
                    >>> # Are you dividing the dot product of the vectors by their lengths?
                    >>> c = calcCosFreqVec(f1,f2)
                    >>> np.isclose(c, 0.932, atol=10**-3, rtol=0)
                    True
                    """
                }
            ],
            'scored': True,
            'setup': r"""
            >>> fn1 = 'Dutch.txt'
            >>> fn2 = 'English.txt'
            >>> f1 = calcFreq(fn1)
            >>> f2 = calcFreq(fn2)
            """,
            'type': 'doctest'
        }
    ]
}
