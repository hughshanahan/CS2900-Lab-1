test = {
    'name': 'checkpoint-1',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems a_2 is undefined. Have you defined it correctly?
                    >>> # I.e. a_2 = ...
                    >>> 'a_2' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your value for the second component of a is incorrect.
                    >>> # Remember that array indexes start from 0 in Python!
                    >>> a_2 != 3
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your value for the second component of a is incorrect.
                    >>> # You should write a[x], where x is the index of the second component.
                    >>> a_2 == 2
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
