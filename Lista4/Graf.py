import networkx as nx
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation

G = nx.connected_watts_strogatz_graph(10, 4, 0.2)  
pos = nx.spring_layout(G)

def Ruch(graf,start):
    Pozycja = start
    while True:
        yield Pozycja
        somsiedzi = list(graf.neighbors(Pozycja))
        if not somsiedzi:
            return
        Pozycja = random.choice(somsiedzi)

def Klatka(num):
    plt.clf()
    node_colors = ['b'] * G.number_of_nodes()
    node_colors[next(Agent)] = 'r' 
    nx.draw(G, pos=pos, node_color=node_colors, with_labels=True)

Agent = Ruch(G, start=0)

aniamcja = animation.FuncAnimation(plt.gcf(),Klatka,frames=range(100),interval=500, repeat=True)
plt.show()




