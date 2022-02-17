import numpy as np

from space import Vector3


class Function3:

    def __init__(self, vect, tStart=0, tEnd=1):
        self.vect = vect
        self.tStart = tStart
        self.tEnd = tEnd

    def evaluate(self, t):
        # print("ev", t)
        if(t <= self.tStart):
            # print("returned", self.start)
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

# Function3.CircleLoop = Function3(
#     (lambda t:
#      Vector3(
#          (np.sin(t/(2*np.pi)))*R if (-np.pi <= t <= np.pi) else t,
#          3*np.tanh(t),
#          (1+np.sin(t/(2*np.pi)))*R if (-np.pi <= t <= np.pi) else 0)),
#     -25, 25)

Function3.CircleLoop = Function3(
    (lambda t:
     Vector3(
         (-np.sin(t))*R if (-np.pi <= t <=
                            np.pi) else (t+np.pi if (t <= 0) else t-np.pi),
         2*np.tanh(t),
         # if (-np.pi <= t <= np.pi) else (2 * np.tanh(-np.pi) if (t <= 0) else 2*np.tanh(np.pi)),
         (1+np.cos(t))*R if (-np.pi <= t <= np.pi) else 0)),
    -25, 25)

Function3.CircleLoopDer1 = Function3(
    (lambda t:
     Vector3(
         (-np.cos(t))*R if (-np.pi <= t <= np.pi) else 1,
         3/(np.cosh(t)**2),
         (-np.sin(t))*R if (-np.pi <= t <= np.pi) else 0)),
    -25, 25)

Function3.CircleLoopDer2 = Function3(
    (lambda t:
     Vector3(
         (np.sin(t))*R if (-np.pi <= t <= np.pi) else 0,
         3*(-2*np.sinh(t))/(np.cosh(t)**3),
         (-np.cos(t))*R if (-np.pi <= t <= np.pi) else 0)),
    -25, 25)

Function3.Line = Function3((lambda t: Vector3(t, 0, 0)), -10, 10)

# # Function3.CircleLoop = Function3(
# #     Vector3(
# #         (lambda t: (np.sin(t/(2*np.pi)))*R if (-np.pi <= t <= np.pi) else t),
# #         (lambda t: 3*np.tanh(t)),
# #         (lambda t: (1+np.sin(t/(2*np.pi)))*R if (-np.pi <= t <= np.pi) else 0)),
# #     -3, 3)
