test = {
    'name': 'checkpoint-4',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Hmm, can't find the dist function. Check the name.
                    >>> # Have you defined it exactly as 'def dist(v)'?
                    >>> "dist" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your function does not return anything!
                    >>> # Make sure you put a return statement at the bottom of the function.
                    >>> dist(v) == None
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # Your function computes the squared distance.
                    >>> # You need to use the math library to square root your answer.
                    >>> dist(v) == 74
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # We're expecting a floating point number here, not an array or integer.
                    >>> # Check that you're computing the distance correctly.
                    >>> type(dist(v)).__name__ in ['float', 'float64']
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your distance calculation is wrong by at least 0.001.
                    >>> # Print out the distance calculated and check it makes sense.
                    >>> np.isclose(dist(v), 8.602, atol=10**-3, rtol=0)
                    True
                    """
                }
            ],
            'scored': True,
            'setup': r"""
            >>> v = np.array([3.,1.,8.])
            """,
            'type': 'doctest'
        }
    ]
}
