import numpy as np
import matplotlib.pyplot as mpl
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint

# https://www.sciencedirect.com/topics/engineering/lorenz-equation - 7.1.1
# equations: sigma * (y - x)
#            x * (rho - z) - y
#           (x * y) - (beta * z)

class lorenz:
    def __init__(self, symbols):
        # check if symbols are positive
        # default to the attractor solution if not
        
        self.allpos = True
        for symbol in symbols:
            if not symbol > 0.0:
                allpos = False
        if self.allpos:
            self.symbols = symbols
        else:
            print("error: all values must be positive- defaulting to [28.0, 10.0, 8.0 / 3.0]")
            # defaults
            self.symbols = [28.0, 10.0, 8.0 / 3.0]     
        
        #self.symbols = [28.0, 10.0, 8.0 / 3.0]
    
    def derivs(self, state, start):
        # function assumes symbols are positive, which should be caught in the constructor
        # unpack symbol and state vectors
        r, s, b = self.symbols
        x, y, z = state
        # return a vector of the three derivs to put into the odeint function
        return s * (y - x), x * (r - z) - y, (x * y) - (b * z)

    def draw(self, time):
        if(not self.allpos):
            print("error: all values must be positive")
            return False;
        initstate = [1.0, 1.0, 1.0]
        # create range of time - 0 -> 40, with steps of param time
        time = np.arange(0.0, 40.0, time)

        poststates = odeint(self.derivs, initstate, time)

        figure = mpl.figure()
        axis = figure.gca(projection = "3d")
        xaxis, yaxis, zaxis = poststates[:, 0], poststates[:, 1], poststates[:, 2]
        axis.plot(xaxis, yaxis, zaxis)
        mpl.draw()
        mpl.show()

def run():
    # init program- get symbol input (default to attractor values), get 
    rho = input("rho value (defaults to 28.0):\n")
    sigma = input("sigma value (defaults to 10.0):\n")
    betai = input("beta value (can be entered in fraction form - defaults to 8.0 / 3.0):\n")
    speed = input("time between evaluation (defaults to 0.01):\n")

    beta = betai

    # handle fraction input
    if("/" in betai):
        betaspl = betai.split("/")
        betaspl[0] = float(betaspl[0].replace(" ", ""))
        betaspl[1] = float(betaspl[1].replace(" ", ""))
        beta = float(betaspl[0] / betaspl[1])

    # sanitize inputs
    try:
        rho = float(rho)
    except:
        if(rho == ""):
            rho = 28.0
        else:
            print("rho: must be number- defaulting to 28.0")
            rho = 28.0

    try:
        sigma = float(sigma)
    except:
        if(sigma == ""):
            sigma = 10.0
        else:
            print("sigma: must be number- defaulting to 10.0")
            sigma = 10.0

    try:
        beta = float(beta)
    except:
        if(beta == ""):
            beta = 8.0 / 3.0
        else:
            print("beta: must be number- defaulting to 8.0 / 3.0")
            beta = 8.0 / 3.0

    try:
        speed = float(speed)
    except:
        if(speed == ""):
            speed = 0.01
        else:
            print("must be decimal number- defaulting to 0.01")
            speed = 0.01

    graph = lorenz([rho, sigma, beta])
    graph.draw(speed)

while True:
    run()
    print("try some new values (ctrl + c to interrupt): ")