test = {
    'name': 'numpy-import',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Numpy has not been imported!
                    >>> # Check that you have executed the 'import numpy as np' code cell!
                    >>>
                    >>> np is not None
                    True
                    """
                }
            ]
        }
    ],
}