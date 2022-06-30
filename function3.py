# Functions that take one float parameter t and return a Vector3.

import numpy as np
from space import Vector3


class Function3:

    def __init__(self, vect, tStart=0, tEnd=1):
        self.vect = vect
        self.tStart = tStart
        self.tEnd = tEnd

    def evaluate(self, t):
        if(t <= self.tStart):
            return self.start
        elif(self.tEnd <= t):
            return self.end
        else:
            return self.vect(t)

    @property
    def start(self): return self.vect(self.tStart)

    @property
    def end(self): return self.vect(self.tEnd)


R = 10

# Function3 representing a perfect cicular loop for a roller coaster layout.
Function3.CircleLoop = Function3(
    (lambda t:
     Vector3(
         (-np.sin(t))*R if (-np.pi <= t <=
                            np.pi) else (t+np.pi if (t <= 0) else t-np.pi),
         2*np.tanh(t),
         (1+np.cos(t))*R if (-np.pi <= t <= np.pi) else 0)),
    -25, 25)
