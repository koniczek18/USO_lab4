import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def zadanie1(active):
    if active:
        # objective function: -y->max
        # change for linprog minimise to accept: y->min
        # other variables: x
        # vector style: [y,x]
        # objective function reflecting vector: [1,0]
        c = np.array([1, 0])
        # 1st constrain: -y+2x<=4
        # 2rd constrain: y+4x>=-2 --> -y-4x<=2
        # 3rd constrain: x+y<3
        # 3rd constrain changed to x+y<=2.999
        A_ub = np.array([[-1, 2], [-1, -4], [1, 1]])
        B_ub = np.array([4, 2, 2.999])
        #calculate
        result = scipy.optimize.linprog(c, A_ub=A_ub, b_ub=B_ub)
        print(result)

if __name__ == '__main__':
    zadanie1(True)
