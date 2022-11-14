import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def przyklad(active):
    if active:
        # objective function: 2x - 3y -> max
        # constrain 1: x + 2y < 4  ->  -x - 2y >= -3.999
        # constrain 2: (1/2)x - y <= 4 -> -(1/2)x + y >= -4
        # constrain 3: (1/2)x - y >= 4 -> ok
        # constrain 4: 12x - 3y <= 6  ->  -12x +3y >= -6
        # constrain 5: 2x + y >= -2
        # DEFINITION: x[0]=x, x[1]=y
        func = lambda x: 2 * x[0] - 3 * x[1]
        cons = ({'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 3.999},
                {'type': 'ineq', 'fun': lambda x: 1 / 2 * x[0] - x[1] - 4},
                {'type': 'ineq', 'fun': lambda x: -12 * x[0] + 3 * x[1] + 6},
                {'type': 'ineq', 'fun': lambda x: 2 * x[0] + x[1] + 2})
        bnds = ((None, None), (None, None))
        result = scipy.optimize.minimize(func, (0, 0), method='SLSQP', bounds=bnds,
                                         constraints=cons)
        print(result.fun)


def zadanie1(active):
    if active:
        # objective function: -y->max
        # other variables: x
        # DEFINITION: x[0]=x, x[1]=y
        # 1st constrain: -y+2x<=4  -> -2x+y>=-4
        # 2rd constrain: 4x+y>=-2
        # 3rd constrain: x+y<3 -> x+y <=2.999
        func = lambda x: 0 * x[0] - x[1]
        cons = ({'type': 'ineq', 'fun': lambda x: -2 * x[0] + x[1] + 4},
                {'type': 'ineq', 'fun': lambda x: 4 * x[0] + x[1] + 2},
                {'type': 'ineq', 'fun': lambda x: x[0] + x[1] - 2.999})
        bnds = ((None, None), (None, None))
        result = scipy.optimize.minimize(func, (0, 0), method='SLSQP', bounds=bnds,
                                         constraints=cons)
        print(result.fun)


def zadanie2(active):
    if active:
        # objective function: x^4-4*x^3-2*x^2+12*x+9 -> min
        # constrain x>=0
        func = lambda x: x ^ 4 - 4 * x ^ 3 - 2 * x ^ 2 + 12 * x + 9
        cons=({'type': 'ineq', 'fun': lambda x: x})
        lw=[0]
        up=np.inf
        result=scipy.optimize.dual_annealing(func,bounds=list(zip(lw,up)))
        print(result.fun)
        #TODO ?????????????????????????????


if __name__ == '__main__':
    przyklad(False)
    zadanie1(False)
    zadanie2(True)
