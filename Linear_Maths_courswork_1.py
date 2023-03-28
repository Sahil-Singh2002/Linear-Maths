def scalar_product(v1,v2):
    """
    Calculate the scalar (dot) product between two vectors, v1 and v2, of arbitrary length.
    """
    # Your code here
    assert type(v1)==tuple and type(v2)==tuple
    assert len(v1)==len(v2)
    for element in v1:
        assert type(element)==int or type(element)==float
    for element in v2:
        assert type(element)==int or type(element)==float
    total_sum = 0
    for i in range(0,len(v1)):
        product= v1[i] *v2[i]
        total_sum += product
    return total_sum

import math
def vector_perpendicular(P,Q):
    """
    Find a vector that is perpendicular to the line between two points P and Q in the plane. 
    """
    # Your code here
    PQ= (Q[0]-P[0],Q[1]-P[1])
    PQ_norm= (P[1]-Q[1],Q[0]-P[0])
    return PQ_norm

