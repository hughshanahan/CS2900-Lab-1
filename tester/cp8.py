test = {
    'name': 'checkpoint-8',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems cDE is undefined. Have you defined it correctly?
                    >>> # I.e. cDE = ...
                    >>> 'cDE' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems cDu is undefined. Have you defined it correctly?
                    >>> # I.e. cDu = ...
                    >>> 'cDu' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems cEu is undefined. Have you defined it correctly?
                    >>> # I.e. cEu = ...
                    >>> 'cEu' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your calculation of cDE is wrong by at least 0.001.
                    >>> # Check if it is following the calculation described in this notebook.
                    >>> np.isclose(cDE, 0.932, atol=10**-3, rtol=0)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your calculation of cDu is wrong by at least 0.001.
                    >>> # Check if it is following the calculation described in this notebook.
                    >>> np.isclose(cDu, 0.927, atol=10**-3, rtol=0)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your calculation of cEu is wrong by at least 0.001.
                    >>> # Check if it is following the calculation described in this notebook.
                    >>> np.isclose(cEu, 0.992, atol=10**-3, rtol=0)
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
