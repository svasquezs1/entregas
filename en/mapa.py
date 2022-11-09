from geopy.distance import great_circle# import folium package
import folium
import math
import sys
import pandas as pd
import numpy as np


my_map4 = folium.Map(location = [6.244203, -75.5812119],
                                        zoom_start = 12)
 
folium.Marker([6.244203, -75.5812119],
              popup = 'Delhi').add_to(my_map4)
 
folium.Marker([6.3271652, -75.571391],
              popup = 'GeeksforGeeks').add_to(my_map4)
 
# Add a line to the map by using line method .
# it connect both coordinates by the line
# line_opacity implies intensity of the line
 
folium.PolyLine(locations = [(6.244203, -75.5812119), (6.3271652, -75.571391)],
                line_opacity = 0.5).add_to(my_map4)
 
my_map4.save("my_map4.html")

# Loading the lat-long data for Kolkata & Delhi
src = (6.244203, -75.5812119)
dest = (6.3271652, -75.571391)
  
# Print the distance calculated in km
print(great_circle(src, dest).km)


acoso = pd.read_csv('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/calles_de_medellin_con_acoso.csv', sep=';')
print(acoso)
poligono = pd.read_csv('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/poligono_de_medellin.csv', sep=';')
print(poligono)

################################################################################
 
# Cada elemento de este diccionario contiene una posicion del camino, y como 
# valor tiene una lista con el calculo del camino mas corto, y el origen del
# mismo
valores={poligono:[math.inf,""],}
 
# aquí establecemos cada uno de los caminos en una sola dirección y el coste
# que tiene cada camino
caminos=[
    ["Cll10","Cll12",9],
    ["Cll10","Cll14",2],
    ["Cll12","Cll14",6],
    ["Cll12","Cll18",1],
    ["Cll14","Cll20",9],
    ["Cll16","Cll12",3],
    ["Cll16","Cll14",2],
    ["Cll16","Cll18",5],
    ["Cll16","Cll20",6],
    ["Cll18","Cll20",3],
    ["Cll18","Cll22",7],
    ["Cll20","Cll22",4]
]
 
def setValores(origen,destino,valor):
    """
    Función que actualiza el valor del diccionario valores, actualizando
    el valor al mas vajo y indicando de de que punto viene el camino mas corto
    Tiene que recibir:
        origen -> punto inicial
        destino -> punto final
        valor -> valor de ese tramo + el valor que tiene el origen
    Devuelve True o False, dependiendo si ha disminuido el valor entre dos puntos
    """
    if valor<valores[destino][0]:
 
        # guardamos el nuevo valor mas bajo
        valores[destino][0]=valor
 
        # guardamos de donde viene el valor mas bajo
        valores[destino][1]=origen
        return True
    return False
 
# definimos el inicio y el destino
inicio="Cll10"
final="Cll22"
 
valores[inicio][0]=0
 
# realizamos un bucle hasta que no haya ningun otro cambio de valores
while True:
    cancel=True
 
    # recorremos cada uno de los caminos
    for i in caminos:
 
        # enviamos los datos del camino
        if setValores(i[0],i[1],valores[i[0]][0]+i[2]):
            cancel=False
 
        # enviamos los datos del camino de forma invertida
        if setValores(i[1],i[0],valores[i[1]][0]+i[2]):
            cancel=False
 
    # finalizamos el bucle cuando ya no hay ningun cambio en los valores
    if cancel:
        break
 
# iniciamos la busqueda del camino mas corto
camino=[final]
 
while True:
    if camino[-1]==inicio:
        break
    camino.append(valores[camino[-1]][1])
 
print("El camino mas corto desde el punto '{}' y el punto '{}' es: {}".format(inicio, final, camino[::-1]))