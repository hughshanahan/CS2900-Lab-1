test = {
    'name': 'checkpoint-5',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems the unitVec function is not defined. 
                    >>> # Have you defined it correctly? I.e. 'def unitVec(v)'
                    >>> "unitVec" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your function doesn't return the correct type or is None!
                    >>> # It should return an array in this case.
                    >>> type(unitVec(v)).__name__ == 'ndarray'
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, the value returned by your function is wrong.
                    >>> # It's off by at least 0.001. Check you're computing it correctly.
                    >>> np.allclose(unitVec(v), dv, atol=10**-3, rtol=0)
                    True
                    """
                }
            ],
            'scored': True,
            'setup': r"""
            >>> v = np.array([4.,9.,7.])
            >>> dv = np.array([0.33104236, 0.7448453 , 0.57932412])
            """,
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Your function doesn't return the correct type or is None!
                    >>> # It should return a string in this case!
                    >>> type(unitVec(null_vec)).__name__ == 'str'
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your function doesn't return the correct message.
                    >>> # It should tell the user it is a 'null vector'.
                    >>> len(re.findall("[nN]ull\\s*[vV]ector", unitVec(null_vec))) != 0
                    True
                    """
                }
            ],
            'scored': True,
            'setup': r"""
            >>> import re
            >>> null_vec = np.array([0.,0.,0.])
            """,
            'type': 'doctest'
        },
    ]
}
