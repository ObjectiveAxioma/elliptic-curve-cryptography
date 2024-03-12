from ecFiniteField import *
from babyStepGiantStep import *


# This is default information stored at the beginning of the program for ease of use. It is
# used by the diffieHellman and checkPoints methods.
E = EllipticCurve(5, 5, 1, 1)
a = 2
b = 0
P = Point(0, 1, E)
Q = Point(2, 4, E)

# Returns 1 if Q = abP and 0 otherwise. Ths is the decisional Diffie-Hellman problem.
def diffieHellman(Q):
    if Q == a*b*P:
        return 1
    else:
        return 0

print(diffieHellman(Q))
