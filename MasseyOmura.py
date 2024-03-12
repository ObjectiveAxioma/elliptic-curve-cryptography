from ecFiniteField import *
from babyStepGiantStep import *
import random


# Define the curve. This example is only defined for a single curve over a single field,
# as it is a demonstration of the concept, but it could easily be extended.
E = EllipticCurve(5, 5, 1, 1)
order = E.orderOfCurve()


# The message m is selected from a list of nine options:
# "Hello"           --  (0, 1)
# "Yes"             --  (0, 4)
# "No"              --  (2, 1)
# "Bye"             --  (2, 4)
# "Okay"            --  (3, 1)
# "Attack"          --  (3, 4)
# "Wait"            --  (4, 2)
# "See you soon"    --  (4, 3)
# "Please resend"   --  infty
#
# Example: if the message m is "Hello", then the point M = Point(0, 1, E)


# Get the inverse of a mod n.
def getInverse(a, n):
    i = 1
    while i < n:
        if (a*i) % n == 1:
            return i
        i+=1

# Generate random integers ma and mb that are invertible mod the curve order.
ma = random.randint(1, order-1)
mb = random.randint(1, order-1)
while getInverse(ma, order) == None or getInverse(mb, order) == None:
    ma = random.randint(1, order-1)
    mb = random.randint(1, order-1)


# Perform Massey-Omura encryption.
def MasseyOmura(M):
    M1 = Alice(M, 0)
    M2 = Bob(M1, 1)
    M3 = Alice(M2, 2)
    m = Bob(M3, 3)

    return decryptMessage(m)


# Decrypts and prints the message according to the key.
def decryptMessage(m):
    if m == Point(0, 1, E):
        return "Hello"
    elif m == Point(0, 4, E):
        return "Yes"
    elif m == Point(2, 1, E):
        return "No"
    elif m == Point(2, 4, E):
        return "Bye"
    elif m == Point(3, 1, E):
        return "Okay"
    elif m == Point(3, 4, E):
        return "Attack"
    elif m == Point(4, 2, E):
        return "Wait"
    elif m == Point(4, 3, E):
        return "See you soon"
    elif m == Point(float("inf"), float("inf"), E):
        return "Please resend"


# Either applies or removes Alice' lock depending on the step.
def Alice(M, step=0):
    if step == 0:
        return ma*M
    elif step == 2:
        mainv = getInverse(ma, order)
        return mainv*M


# Either adds or removes Bob's lock depending on the step.
def Bob(M, step=1):
    if step == 1:
        return mb*M
    elif step == 3:
        mbinv = getInverse(mb, order)
        m = mbinv*M
        return m
