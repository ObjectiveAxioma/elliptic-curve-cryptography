from ecFiniteField import *
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


# Generate the public key
P = Point(0, 1, E)
s = 6
B = 6*P


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


# Returns 1 when n and m are coprime, 0 otherwise. Used to ensure that k does not divide #E(Fq).
def isCoprime(n, m):
    i = 2
    while i < n and i < m:
        if n % i == 0 and m % i == 0:
            return 0
        i+=1
    return 1


# Alice encrypts her message for Bob to recieve and decrypt.
def Alice(M):
    k = random.randint(1, order-1)
    while not isCoprime(k, order):
        k = random.randint(1, order-1)
    M1 = k*P
    M2 = M + k*B

    return [M1, M2]


# Bob reads Alice' message on the premise that: M2 - sM1 = (M + kB) - s(kP) = M
# Only Bob can do this because no attacker knows k or s, and either would be required
# to recover the original message M from Alice.
def Bob(message):
    M = message[1] - s*message[0]
    return M


# Demonstrates ElGamal public key encryption using the Alice and Bob methods.
def ElGamalPKE(M):
    message = Alice(M)
    m = Bob(message)
    
    return decryptMessage(m)
