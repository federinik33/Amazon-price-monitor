import matplotlib.pyplot as plt
import numpy as np;
#import scipy.optimize as opt;
import datetime
import os

files = os.listdir()
j=0
while(j<len(files)):
	print(j,files[j])
	j+=1
N=int(input("Quanti grafici vuoi disegnare? "))
lista=[]
j=0
while(j<N):
	lista.append(int(input("Quale grafico vuoi disegnare? ")))
	j+=1
N=len(lista)
k=0
while(k<N):
    x,y = [],[]
    nome=files[lista[k]]
    start=0
    end=4
    mass=0
    p_mass=0
    list = open(nome, "r").readlines()
    for i, dati in enumerate(list):
        a=dati.split()[0]
        b=dati.split()[1]+" "+dati.split()[2]
        if(float(a)>9999):
            pass
        else:
            x.append(datetime.datetime.strptime(b, '%d/%m/%y %X'))
            y.append(float(a))
        
        
    #plt.plot(x,y)  #comando che disegna un grafico, quindi unisce i punti
    plt.xlabel("data")
    plt.ylabel("prezzo")
    plt.title(nome)
    plt.legend(nome.split())
    plt.scatter(x=x,y=y)
    plt.show()
    k+=1

# Show the graph


