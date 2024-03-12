from ecFiniteField import Point, EllipticCurve

def babyStepGiantStep(curve, P, Q):
    if not isinstance(curve, EllipticCurve) or not isinstance(P, Point) or not isinstance(Q, Point):
        return "Please pass an EllipticCurve and two Point objects."

    # Get an integer with a value greater than q**(1/2).
    N = curve.orderOfCurve()
    m = int(curve.q**(1/2) + 1)

    # Find all values of jP for 0 <= j < m.
    i = 0
    iP = []
    while i < m:
        iP.append(i*P)
        i+=1

    # Compute Q - jmP for all 0 <= j < m and check if there is a match.
    j = 0
    isMatch = 0
    while j < m and isMatch == 0:
        point = Q - j*m*P
        i = 0
        while i < m and isMatch == 0:
            if point == iP[i]:
                isMatch = 1
            i+=1
        j+=1

    # Compute and return i + j*m when there is a match.
    k = ((i-1) + (j-1)*m) % N

    return k
