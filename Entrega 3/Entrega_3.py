import pandas as pd
import networkx as nx
import folium

#-----Pone el archivo en un DataFrame-----#
datos = pd.read_csv('calles.csv',header=0)
#print(datos)
#origin2 es el primero en el mapa de folium (6,040545, -75,35535) y lo mismo para destination2
datos[["origin", "origin2"]] = datos["origin"].str.split(", ", expand=True)
datos[["destination", "destination2"]] = datos["destination"].str.split(", ", expand=True)
#print(datos)
dt = pd.read_csv('hola.csv', header=0, sep=",")
print(dt)
#datos.to_csv('hola.csv', index=False)
#dt = datos.get("origin")
#print(datos)
#dt.split(sep=",", maxsplit=-1) 
#new = dt._getitem_(1)
#dt_list = new.split(", ")
#print(dt_list)
#new = []
#for i in range(0, 68000):
    #new.append(dt._getitem_(i))
#new.reverse()
#print(dt)
print("Dataframe Listo!")

#-----Poligono de la ciudad de Medellín-----#
poligono = pd.read_csv('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/poligono_de_medellin.csv', sep=';')
#print(poligono)
#print("Poligono listo!")
#-----Ingresamos los datos a un grafo-----# Es decir, el grafo es DG

DG = nx.DiGraph()
for row in datos.iterrows():
    DG.add_edge(row[1]["origin2"],row[1]["origin"],oneway = row[1]["oneway"])
print(DG)
#ista = list[DG.add_edge(row[1]["origin"],row[1]["harassmentRisk"])]
src = dt.get("origin2")
dest = dt.get("origin")
src2 = dt.get("destination2")
dest2 = dt.get("destination")
my_map = folium.Map(location = [src[1], dest[1]], zoom_start = 12)
my_map.save("my_mapp.html")

#Idea: ir mostrando un marker en el folium
def dijkstra(inicio, destino, peso):
    peso = dt.get("harassmentRisk")
    for i in range(0, 68749):
        if dest[i] == src2[i]: