import matplotlib.pyplot as plt
from ModelSEIR import Dane,Time, N
from numpy import linspace
fig, axs = plt.subplots(ncols=2, nrows=2)
WykresGlowny = axs[0,0]
WykresBeta = axs[1,0]
WykresSigma = axs[0,1]
WykresGamma = axs[1,1]

Wykresy = [WykresGlowny,WykresBeta,WykresSigma,WykresGamma]

xticks = linspace(0,100,11)
yticks = linspace(0,N,11)

NazwyWykresow = ['Wykres Zadanie','Wykres Beta * 2','Wykres Sigma * 2','Wykres Gamma * 0.5']
for i ,Wykres  in enumerate(Wykresy):
    Wykres.plot(Time, Dane[i][:,0], 'b', label='Podatni')
    Wykres.plot(Time, Dane[i][:,1], 'y', label='Wystawieni')
    Wykres.plot(Time, Dane[i][:,2], 'r', label='Zakażeni')
    Wykres.plot(Time, Dane[i][:,3], 'g', label='Wyleczeni')
    Wykres.set_title(NazwyWykresow[i])
    Wykres.set_xlabel('Czas (dni)')
    Wykres.set_ylabel('Liczba osób')
    Wykres.legend()
    Wykres.grid()
    Wykres.set_xticks(xticks)

fig.tight_layout()
plt.show()
