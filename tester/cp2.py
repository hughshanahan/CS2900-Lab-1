test = {
    'name': 'checkpoint-2',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems b is undefined. Have you defined it correctly?
                    >>> # I.e. b = np.array( . . . )
                    >>> "b" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, b is not of type float64.
                    >>> # Check you have specified the type correctly.
                    >>> b.dtype.name
                    'float64'
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, b is the correct type but the values are wrong. Test
                    >>> # Check the numbers you specified for the elements of b.
                    >>> b.dtype.name == 'float64' and np.array_equal(b, np.array([4., 5., 6.]))
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
