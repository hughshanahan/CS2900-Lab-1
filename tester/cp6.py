test = {
    'name': 'checkpoint-6',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Hmm, can't find the calcFreq function. Check the name.
                    >>> # Have you defined it exactly as 'def calcFreq(fileName)'?
                    >>> "calcFreq" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your function does not return a vector!
                    >>> # Make sure you put a return statement at the bottom of the function.
                    >>> f = calcFreq(fn)
                    >>> type(f).__name__ in ['numpy.ndarray']
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # calcFreq computes the frequency vector of the individual letters.
                    >>> # The size of the frequency vector should be the same as the
                    >>> # number of letters in the alphabet.
                    >>> f = calcFreq(fn)
                    >>> len(f) == 26
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # We're expecting that the entries are floating point numbers, not an array or integer.
                    >>> # Check that you're computing the frequency correctly.
                    >>> f = calcFreq(fn)
                    >>> type(f[25]).__name__ in ['float', 'float64']
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your frequency calculation is wrong by at least 0.001.
                    >>> # Print out the frequencies and check that they make sense.
                    >>> # Are all the entries less than 1?
                    >>> # If you sum up the frequencies do they add to 1?
                    >>> # Letters like 'e' and 'a' should be more common than 'x'
                    >>> f = calcFreq(fn)
                    >>> np.isclose(f[4], 0.192, atol=10**-3, rtol=0)
                    True
                    """
                }
            ],
            'scored': True,
            'setup': r"""
            >>> fn = 'Dutch.txt'
            """,
            'type': 'doctest'
        }
    ]
}
