def scalar_product(v1, v2):
    """
    Calculate the scalar (dot) product between two vectors, v1 and v2, of arbitrary length.

    Parameters:
        v1 (tuple): First vector.
        v2 (tuple): Second vector.

    Returns:
        float: Scalar product of v1 and v2.
    """
    assert isinstance(v1, tuple) and isinstance(v2, tuple)
    assert len(v1) == len(v2)
    assert all(isinstance(element, (int, float)) for element in v1)
    assert all(isinstance(element, (int, float)) for element in v2)
    
    return sum(v1[i] * v2[i] for i in range(len(v1)))


def vector_perpendicular(P, Q):
    """
    Find a vector that is perpendicular to the line between two points P and Q in the plane.

    Parameters:
        P (tuple): First point.
        Q (tuple): Second point.

    Returns:
        tuple: Perpendicular vector.
    """
    PQ = (Q[0] - P[0], Q[1] - P[1])
    PQ_norm = (PQ[1], -PQ[0])
    return PQ_norm


def intersection_lines(L1, L2):
    """
    Find the intersection point of the two lines L1 and L2 given by two tuples L1=(P1, v1) and L2=(P2, v2)
    where the points P1, P2 and the vectors v1, v2 are all represented by tuples of length 2.

    If the vectors v1 and v2 are parallel, an assertion error is raised.

    Parameters:
        L1 (tuple): Line 1 represented as (P1, v1).
        L2 (tuple): Line 2 represented as (P2, v2).

    Returns:
        tuple: Intersection point.

    Raises:
        AssertionError: If the vectors v1 and v2 are parallel.
    """
    a1, c1 = L1[0]
    b1, d1 = L1[1]
    a2, c2 = L2[0]
    b2, d2 = L2[1]

    mag_v1 = math.sqrt(b1 ** 2 + d1 ** 2)
    mag_v2 = math.sqrt(b2 ** 2 + d2 ** 2)

    assert not (b1 * mag_v2 == b2 * mag_v1 and d1 * mag_v2 == d2 * mag_v1)

    s = ((c2 * b2) + (d2 * a1) - (d2 * a2) - (c1 * b2)) / ((d1 * b2) - (b1 * d2))

    return (a1 + s * b1, c1 + s * d1)
