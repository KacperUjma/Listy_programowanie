from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-S0",default=999,type=int)
parser.add_argument("-E0",default=1,type=int)
parser.add_argument("-I0",default=0,type=int)
parser.add_argument("-R0",default=0,type=int)
parser.add_argument("-beta",default=1.34,type=float)
parser.add_argument("-sigma",default=0.19,type=float)
parser.add_argument("-gamma",default=0.34,type=float)

args = parser.parse_args()


S0 = args.S0
E0 = args.E0
I0 = args.I0
R0 = args.R0
N = int(S0 + E0 + I0 + R0)

beta = args.beta
sigma = args.sigma
gamma = args.gamma

Time = np.linspace(1, 100, 100)

def SEIR(SEIR, t, beta, sigma, gamma):
    S, E, I, R = SEIR

    dSdt = -beta*S*I/N
    dEdt = beta*S*I/N - sigma*E
    dIdt = sigma*E - gamma*I
    dRdt = gamma*I

    return dSdt, dEdt, dIdt, dRdt

SEIR0 = [S0,E0,I0,R0]
Parametry = (beta,sigma,gamma)
Rozwiazanie = odeint(SEIR,SEIR0,Time,args=Parametry)
Dane = []

Dane.append(odeint(SEIR,SEIR0,Time,args=Parametry))
# β to wskaźnik infekcjii (tempo jej rozprzestrzeniania się),
Parametry = (2*beta,sigma,gamma)

Dane.append(odeint(SEIR,SEIR0,Time,args=Parametry))
# σ to wskaźnik ikubacji (średni czas inkubacji to 1/σ),
Parametry = (beta,2*sigma,gamma)

Dane.append(odeint(SEIR,SEIR0,Time,args=Parametry))
# γ to wskaźnik wyzdrowień (jeśli średni czas infekcji wynosi D, wówczas γ = 1/D).
Parametry= (beta,sigma,0.5*gamma)

Dane.append(odeint(SEIR,SEIR0,Time,args=Parametry))


