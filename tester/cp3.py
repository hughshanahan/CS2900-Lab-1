test = {
    'name': 'checkpoint-3',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems co is undefined. Have you defined it correctly?
                    >>> # I.e. co = np.array( . . . )
                    >>> "co" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # co is not the same dimensions as c!
                    >>> # co should be defined as a vector [u1, u2]
                    >>> c.shape == co.shape
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, co is not orthogonal to c.
                    >>> # Recall what it means for a vector to be orthogonal to another.
                    >>> from tester.utils.cp3 import check_orthogonal
                    >>> check_orthogonal(c, co)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, p is not defined correctly!
                    >>> # You should set p equal to your check for orthogonality.
                    >>> # p = . . .
                    >>> "p" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # p is not equal to zero.
                    >>> # Check that your vectors are orthogonal.
                    >>> p == 0
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, p is zero but you seem to have set it equal to 
                    >>> # zero manually. This wasn't really the idea...
                    >>> # You need to check orthogonality properly.
                    >>> from tester.utils.cp3 import check_p
                    >>> check_p()
                    True
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
