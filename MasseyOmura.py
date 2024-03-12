from ecFiniteField import *
from babyStepGiantStep import *

E = curve(5, 5, 1, 1)

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

M = Point(0, 1, E)
