'''
This module contains functions for vector operations.
'''

def add(v1, v2):
    '''Add two vectors.'''
    if len(v1) != len(v2):
        raise ValueError('Vectors must have the same length.')
    return [v1[i] + v2[i] for i in range(len(v1))]

def scamul(v, s):
    '''Scalar multiplication of a vector.'''
    return [x * s for x in v]

def dot(v1, v2):
    '''Dot product of two vectors.'''
    if type(v2) == str:
        return sdot(v1, v2)
    elif len(v1) != len(v2):
        raise ValueError('Vectors must have the same length.')
    return sum([v1[i] * v2[i] for i in range(len(v1))])

def sdot(v, option='sum', *args):
    '''special dot products of a vector.'''
    match option:
        case 'sum':
            return sum(v)
        case 'mean':
            return sum(v) / len(v)
        case 'unit':
            return v[args[0]]
        case 'sumsq':
            return sum([x**2 for x in v])
        case default:
            raise ValueError('Invalid option. Use "sum", "mean", "unit" or "sumsq".')

def norm(v):
    '''Norm of a vector.'''
    return (sdot(v, 'sumsq'))**0.5

def unit(v):
    '''Unit vector.'''
    return scamul(v, 1/norm(v))

def lincomb(vlist, c = None):
    '''Linear combination of vectors.
    Returns the linear combination of the vectors in vlist with coefficients in c.
    If c is a scalar, all vectors are multiplied by c. If c is None, all coefficients are 1.'''
    if c is None or type(c) == int or type(c) == float:
        c = [1] * len(vlist) if c is None else [c] * len(vlist)
    if len(vlist) != len(c):
        raise ValueError('The number of coefficients must match the number of vectors.')
    return [sum([c[i] * vlist[i][j] for i in range(len(vlist))]) for j in range(len(vlist[0]))]


