def evklid_algorithm(a: int, b: int):
    '''
    Returns the GCD(greatest common divisor) between a and b numbers.
    >>> evklid_algorithm(30, 5)
    5
    >>> evklid_algorithm(6, 5)
    1
    >>> evklid_algorithm(30, -1)
    1
    '''
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return evklid_algorithm(b, a % b)
