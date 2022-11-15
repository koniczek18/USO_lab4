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
        func = lambda x: -2 * x[0] + 3 * x[1]
        cons = ({'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 3.999},
                {'type': 'ineq', 'fun': lambda x: 1 / 2 * x[0] - x[1] - 4},
                {'type': 'ineq', 'fun': lambda x: -12 * x[0] + 3 * x[1] + 6},
                {'type': 'ineq', 'fun': lambda x: 2 * x[0] + x[1] + 2})
        bnds = ((None, None), (None, None))
        result = scipy.optimize.minimize(func, (0, 0), method='SLSQP', bounds=bnds,
                                         constraints=cons)
        print('Przyklad')
        print('x',result.x[0])
        print('y',result.x[1])


def zadanie1(active):
    if active:
        # objective function: -y->max
        # other variables: x
        # DEFINITION: x[0]=x, x[1]=y
        # 1st constrain: -y+2x<=4  -> -2x+y>=-4
        # 2rd constrain: 4x+y>=-2
        # 3rd constrain: x+y<3 -> -x-y>=-2.999
        func = lambda x: 0 * x[0] + x[1]
        cons = ({'type': 'ineq', 'fun': lambda x: -2 * x[0] + x[1] + 4},
                {'type': 'ineq', 'fun': lambda x: 4 * x[0] + x[1] + 2},
                {'type': 'ineq', 'fun': lambda x: -(x[0] + x[1] - 2.999)})
        bnds = ((None, None), (None, None))
        result1 = scipy.optimize.minimize(func, (0, 0), method='SLSQP', bounds=bnds,
                                         constraints=cons)

        print('Zadanie1')
        print('x',result1.x[0])
        print('y',result1.x[1])


def zadanie2(active):
    if active:
        # objective function: x^4-4*x^3-2*x^2+12*x+9 -> min
        # constrain x>=0
        func = lambda x: pow(x,4) - 4 * pow(x,3) - 2 * pow(x,2) + 12*x + 9
        cons=({'type': 'ineq', 'fun': lambda x: x})
        result1 = scipy.optimize.minimize(func,(2), bounds=[(0,100000)])
        print(result1.x)
        #lw=[0]*10
        #up=np.inf
        #result2=scipy.optimize.dual_annealing(func,bounds=scipy.optimize.Bounds([0],[np.inf]))

def model(x,t,a0,a1,a2,a3):
    x=a0+a1*t+a2*pow(t,2)+a3*pow(t,3)
    dx=a1+a2*t+a3*pow(t,2)
    J=24*x*t+2*dx*dx-4*t
    return J

def problem_dyn(a):
    a0,a1,a2,a3=a
    t=np.linspace(0,1,101)
    sol=odeint(model,0,t,args=(a0,a1,a2,a3))

def zadanie3(active):
    if active:
        cons1=scipy.optimize.LinearConstraint([1,0,0,0],lb=1,ub=1)
        cons2=scipy.optimize.LinearConstraint([1,1,1,1],lb=3,ub=3)
        result=scipy.optimize.minimize(problem_dyn,(0,0,0,0),constraints=(cons1,cons2))
        #TODO help me

if __name__ == '__main__':
    przyklad(False)
    zadanie1(False)
    zadanie2(False)
    zadanie3(True)
