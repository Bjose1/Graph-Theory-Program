from Grafo import Grafo
from Nodo import Nodo
from Semaforo import Semaforo
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import random 
import  numpy as np
import pandas as pd

grafo = Grafo()
nodos = [
    # Nodo 1
    Nodo(
        nombre="Cll94-cra52",
        info=[Semaforo(tv=27, tr=58, c=2)],
        nodos_ady_salida=["Cll94-cra53"], 
        peso_aristas_salida=[260],
        referencia=["patinodromo"]
    ),
    
    # Nodo 2
    Nodo(
        nombre="Cll98-cra52",
        info=[Semaforo(tv=45, tr=75, c=18)],
        nodos_ady_salida=["Cll94-cra52"], 
        peso_aristas_salida=[320],
        referencia=["farmanorte"]
    ),
    
    # Nodo 3    2   4
    Nodo(
        nombre="Cll99-cra52",
        info=[Semaforo(tv=55, tr=66, c=3), Semaforo(tv=48, tr=70, c=16)],
        nodos_ady_salida=["Cll98-cra52", "Cll99-cra53"], 
        peso_aristas_salida=[92, 230],
        referencia=["alkosto2", "exito"]
    ),
    
    # Nodo 4    3   9    11pen y 14ult
    Nodo(
        nombre="Cll99-cra53",
        info=[Semaforo(tv=1, tr=1, c=40), Semaforo(tv=48, tr=70, c=9), Semaforo(tv=1, tr=1, c=34), Semaforo(tv=1, tr=1, c=34)],
        nodos_ady_salida=["Cll99-cra52", "Cll98-cra53", "Cll100-cra55", "Cll99-cra55" ], 
        peso_aristas_salida=[230, 125, 116, 90],
        referencia=["buenavista2", "carrera532", "mall1", "pp1"]
    ),
    
    # Nodo 5
    Nodo(
        nombre="Cll99-cra56",
        info=[Semaforo(tv=48, tr=50, c=32)],
        nodos_ady_salida=["Cll98-cra56"], 
        peso_aristas_salida=[170],
        referencia=["olimpica"]
    ),
    
    # Nodo 6    7       15
    Nodo(
        nombre="Cll98-cra56",
        info=[Semaforo(tv=45, tr=75, c=20), Semaforo(tv=1, tr=1, c=15)],
        nodos_ady_salida=["Cll94-cra56", "Cll98-cra55"],
        peso_aristas_salida=[450, 250],
        referencia=["iglesiaes", "pp2"]
    ),
    
    # Nodo 7
    Nodo(
        nombre="Cll94-cra56",
        info=[],
        nodos_ady_salida=[],
        peso_aristas_salida=[],
        referencia=[]
    ),
    
    # Nodo 8        7       9
    Nodo(
        nombre="Cll94-cra53",
        info=[Semaforo(tv=85, tr=42, c=24), Semaforo(tv=85, tr=42, c=11)],
        nodos_ady_salida=["Cll94-cra56", "Cll98-cra53"],
        peso_aristas_salida=[215, 315],
        referencia=["parquebosquesdelnorte", "mcdonalds1"]
    ),
    
    # Nodo 9    4       10  
    Nodo(
        nombre="Cll98-cra53",
        info=[Semaforo(tv=48, tr=70, c=20), Semaforo(tv=1, tr=1, c=14)],
        nodos_ady_salida=["Cll99-cra53", "Cll98-cra52c"],
        peso_aristas_salida=[125, 180],
        referencia=["carrera531", "buenavista1"]
    ),
    
    # Nodo 10
    Nodo(
        nombre="Cll98-cra52c",
        info=[Semaforo(tv=30, tr=80, c=20)],
        nodos_ady_salida=["Cll98-cra52"],
        peso_aristas_salida=[110],
        referencia=["alkosto"]
    ),
    
    # Nodo 11
    Nodo(
        nombre="Cll100-cra55",
        info=[Semaforo(tv=30, tr=60, c=10)],
        nodos_ady_salida=["Cll99a-cra55"],
        peso_aristas_salida=[100],
        referencia=["carrera55"]
    ),
    
    # Nodo 12       5    4 nuevo
    Nodo(
        nombre="Cll99-cra56p",
        info=[Semaforo(tv=40, tr=70, c=16) , Semaforo(tv=48, tr=76, c=10)],
        nodos_ady_salida=["Cll99-cra56", "Cll99-cra53"],
        peso_aristas_salida=[125, 140],
        referencia=["carrera56", "mall4"]
    ),
    
    # Nodo 13
    Nodo(
        nombre="Cll99a-cra55",
        info=[Semaforo(tv=37, tr=62, c=17), Semaforo(tv=40, tr=75, c=15)],
        nodos_ady_salida=["Cll99-cra56p", "Cll99-cra55"],
        peso_aristas_salida=[216, 116],
        referencia=["hotelcp", "mall2"]
    ),
    
    # Nodo 14       5   4
    Nodo(
        nombre="Cll99-cra55",
        info=[Semaforo(tv=1, tr=1, c=40), Semaforo(tv= 40, tr=67, c=34)],
        nodos_ady_salida=["Cll99-cra56", "Cll99-cra53"],
        peso_aristas_salida=[300, 116],
        referencia=["calle99", "mall3"]
    ),
    
    # Nodo 15
    Nodo(
        nombre="Cll98-cra55",
        info=[Semaforo(tv=28, tr=61, c=21)],
        nodos_ady_salida=["Cll98-cra53"],
        peso_aristas_salida=[150],
        referencia=["mcdonalds2"]
    )
]
for nodo in nodos:
    grafo.agregar_nodo(nodo)
    
#grafo.mostrar_adyacencias()
#grafo.mostrar_referencias()
#print(grafo.get_trayecto("Calle84-cra44", "Calle86-cra43"))
#print(grafo.get_referencia("Calle-72-cra-15","Calle-45-cra-30"))
#print(grafo.trayecto_referencia("Almacén Olímpica", "Universidad Autónoma"))
#grafo.mostrar_pesos("Calle84-cra44")
for nodo in nodos:
    grafo.mostrar_pesos(nodo.nombre)
    
seed = 0 
random.seed(seed)
np.random.seed(seed)
    
def crear_grafo(rojas):
    G=nx.MultiDiGraph()
    rojas = [p.replace(" ","").lower() for p in rojas]
    print("rojas",rojas)
    G.add_node("1")
    G.add_node("2")
    G.add_node("3")
    G.add_node("4")
    G.add_node("5")
    G.add_node("6")
    G.add_node("7")
    G.add_node("8")
    G.add_node("9")
    G.add_node("10")
    G.add_node("11")
    G.add_node("12")
    G.add_node("13")
    G.add_node("14")
    G.add_node("15")
    
    ubicacion= {
        "1":(-6,3),
        "2":(-1.5,3),
        "3":(6,3),
        "4":(6,2),
        "5":(5.5,1),
        "6":(-1.5,1),
        "7":(-6,1),
        "8":(-6,2),
        "9":(-1.5,2),
        "10":(-1.5,2.5),
        "11":(13,1.8),
        "12":(7,1),
        "13":(10,1.5),
        "14":(5.5,1.5),
        "15":(-1.5,1.5)
    }

    

    fig, ax= plt.subplots(figsize=(3,3))
    ax.set_title("Sector Buenavista")

    G.add_edge("2", "1",key="farmanorte" ,nombre="96")
    G.add_edge("5", "6",key="olimpica", nombre="56")
    G.add_edge("6", "7",key="iglesiaespiritusanto" ,nombre="38")
    G.add_edge("8", "7",key="parquebosquesdelnorte" , nombre="26")
    G.add_edge("1", "8",key="patinodromo" , nombre="11")
    G.add_edge("8", "9",key="mcdonalds1" , nombre="14")
    G.add_edge("9", "10",key="buenavista1" , nombre="18")
    G.add_edge("10", "2",key="alkosto" , nombre="58")
    G.add_edge("6", "15",key="pp2" , nombre="21")
    G.add_edge("15", "9",key="mcdonalds2" , nombre="68")
    G.add_edge("12", "5",key="carrera56" , nombre="\n\n<-\n\n15")
    G.add_edge("11", "13",key="carrera55" , nombre="20")
    G.add_edge("3", "2",key="alkosto" , nombre="5")
    G.add_edge("14","5",key="calle99" ,nombre='38 -')
    G.add_edge("13","14",key="mall2" ,nombre='20')

    nx.draw(G,pos=ubicacion, ax=ax, with_labels=True, node_color="red", edge_color="black",arrows=True,node_size=50,font_size=5)
    edge_labels = {(u, v, k): d["nombre"] for u, v, k, d in G.edges(keys=True, data=True) if "nombre" in d}
    nx.draw_networkx_edge_labels(G, pos=ubicacion, edge_labels=edge_labels, ax=ax,font_size=3,font_color="black",label_pos=0.5,rotate=False)

    if(rojas!=[]):
        ax.clear()
        plt.draw()
        colores_aristas=[]
        for u, v, k in G.edges(keys=True):
            if (k) in rojas:
                color = "red"
            else:
                color = "black"
            colores_aristas.append(color)
        
        nx.draw(G,pos=ubicacion, ax=ax, with_labels=True, node_color="red", edge_color=colores_aristas,arrows=True,node_size=50,font_size=5)
        edge_labels = {(u, v, k): d["nombre"] for u, v, k, d in G.edges(keys=True, data=True) if "nombre" in d}
        nx.draw_networkx_edge_labels(G, pos=ubicacion, edge_labels=edge_labels, ax=ax,font_size=3,font_color="black",label_pos=0.5,rotate=False)

    if("carrera531" in rojas):
        color="red"
    else:
        color="black"
    nx.draw_networkx_edges(
        G, pos=ubicacion, ax=ax,
        edgelist=[("9", "4", "camino 1")],
        connectionstyle="arc3,rad=-0.2",
        arrows=True, edge_color=color
    )
    edge_labels = {("9", "4","Camino 1"):"24\n\n\n\n\n"}

    nx.draw_networkx_edge_labels(
        G, pos=ubicacion, edge_labels=edge_labels, ax=ax,
        font_color="black",font_size=4, label_pos=0.5,rotate=False
    )
    
    if("carrera532" in rojas):
        color="red"
    else:
        color="black"
    nx.draw_networkx_edges(
        G, pos=ubicacion, ax=ax,
        edgelist=[("4", "9", "camino 2")],
        connectionstyle="arc3,rad=-0.2",
        arrows=True, edge_color=color
    )
    edge_labels = {("4", "9","Camino 2"):"\n\n13"}

    nx.draw_networkx_edge_labels(
        G, pos=ubicacion, edge_labels=edge_labels, ax=ax,
        font_color="black",font_size=4, label_pos=0.5,rotate=False
    )

    if("exito" in rojas):
        color="red"
    else:
        color="black"
    nx.draw_networkx_edges(
        G, pos=ubicacion, ax=ax,
        edgelist=[("3", "4", "camino 6")],
        connectionstyle="arc3,rad=0.3",
        arrows=True, edge_color=color
    ) 
    edge_labels = {("4", "3","Camino 6"):"                           24"}

    nx.draw_networkx_edge_labels(
        G, pos=ubicacion, edge_labels=edge_labels, ax=ax,
        font_color="black",font_size=4, label_pos=0.5,rotate=False
    )

    if("buenavista2" in rojas):
        color="red"
    else:
        color="black"
    nx.draw_networkx_edges(
        G, pos=ubicacion, ax=ax,
        edgelist=[("4", "3", "camino 7")],
        connectionstyle="arc3,rad=0.3",
        arrows=True, edge_color=color
    )
    edge_labels = {("4", "3","Camino 7"):"45             "}

    nx.draw_networkx_edge_labels(
        G, pos=ubicacion, edge_labels=edge_labels, ax=ax,
        font_color="black",font_size=4, label_pos=0.5,rotate=False
    )

    if("hotelcp" in rojas):
        color="red"
    else:
        color="black"
    nx.draw_networkx_edges(
        G, pos=ubicacion, ax=ax,
        edgelist=[("13", "12", "camino 8")],
        connectionstyle="arc3,rad=-0.3",
        arrows=True, edge_color=color
    )
    edge_labels = {("13", "12","Camino 7"):"         26"}
    nx.draw_networkx_edge_labels(
        G, pos=ubicacion, edge_labels=edge_labels, ax=ax,
        font_color="black",font_size=3, label_pos=0.5,rotate=False
    )

    if("mall4" in rojas):
        color="red"
    else:
        color="black"
    nx.draw_networkx_edges(
        G, pos=ubicacion, ax=ax,
        edgelist=[("12", "4", "camino 9")],
        connectionstyle="arc3,rad=0.3",
        arrows=True, edge_color=color
    )
    edge_labels = {("12", "4","Camino 7"):"         21"}
    nx.draw_networkx_edge_labels(
        G, pos=ubicacion, edge_labels=edge_labels, ax=ax,
        font_color="black",font_size=3.3, label_pos=0.3,rotate=False
    )

    if("mall1" in rojas):
        color="red"
    else:
        color="black"
    nx.draw_networkx_edges(
        G, pos=ubicacion, ax=ax,
        edgelist=[("4", "11", "camino 10")],
        connectionstyle="arc3,rad=-0.3",
        arrows=True, edge_color=color
    )
    edge_labels = {("4", "11","Camino 4"):"36\n\n"}

    nx.draw_networkx_edge_labels(
        G, pos=ubicacion, edge_labels=edge_labels, ax=ax,
        font_color="black",font_size=3.5, label_pos=0.5,rotate=False
    )

    if("mall3" in rojas):
        color="red"
    else:
        color="black"
    nx.draw_networkx_edges(
        G, pos=ubicacion, ax=ax,
        edgelist=[("14", "4", "camino 11")],
        connectionstyle="arc3,rad=0.2",
        arrows=True, edge_color=color
    )
    edge_labels = {("14", "4","Camino 4"):"      47"}

    nx.draw_networkx_edge_labels(
        G, pos=ubicacion, edge_labels=edge_labels, ax=ax,
        font_color="black",font_size=3, label_pos=0.2,rotate=False
    )

    if("pp1" in rojas):
        color="red"
    else:
        color="black"
    nx.draw_networkx_edges(
        G, pos=ubicacion, ax=ax,
        edgelist=[("4", "14", "camino 11")],
        connectionstyle="arc3,rad=0.3",
        arrows=True, edge_color=color
    )
    edge_labels = {("4", "14","Camino 4"):"36       "}

    nx.draw_networkx_edge_labels(
        G, pos=ubicacion, edge_labels=edge_labels, ax=ax,
        font_color="black",font_size=3, label_pos=0.1,rotate=False
    )
    
    st.pyplot(fig)


st.title("🗺️ Caminos de Buenavista")

datos_nodos = {
    "Interseccion": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    "Direccion": ["Cll94-cra52", "Cll98-cra52", "Cll99-cra52", "Cll99-cra53", "Cll99-cra56", "Cll98-cra56", "Cll94-cra56", "Cll94-cra53", "Cll98-cra53", "Cll98-cra52c", "Cll100-cra55", "Cll99-cra56p", "Cll99a-cra55", "Cll99-cra56", "Cll98-cra55"]
}

# Crear DataFrame
df1 = pd.DataFrame(datos_nodos)

datos_aristas = {
    "Arista": ["1->8", "8->7","8->9","2->1","10->2","9->10","15->9","6->15","9->4","6->7","3->2","3->4","4->3","4->9","4->11","4->14","14->4","14->5","12->5","12->4","13->14","13->12","11->13","5->6"],
    "Referencua": ["Patinodromo", "Parque Bosques del Norte", "Mc Donalds 1", "Farma Norte", "Alkosto", "Buenavista 1", "Mc Donalds 2", "Plaza del Parque 2", "Carrera 53 1", "Iglesia Espiritu Santo", "Alkosto", "Exito", "Buenavista 2", "Carrera 53 2", "Mall 1","Plaza del Parque 1","Mall 3", "Calle 99","Carrera 56 ","Mall 4","Mall 2","Hotel CP","Carrera 55 ","Olimpica"]
}

# Crear DataFrame
df2 = pd.DataFrame(datos_aristas)





col1, col2 = st.columns([2, 1])

with col1:
    crear_grafo([])
    with col2:
        desde = st.text_input("¿Dónde te ubicas?")
        hacia = st.text_input("¿A dónde quieres ir?")
    #desde=(desde.replace(" ","").lower())
    #hacia=(hacia.replace(" ","").lower())
        if st.button("Buscar"):
            with col1:
                if not desde.strip() or not hacia.strip() or grafo.existe_nodo(desde)==False or grafo.existe_nodo(hacia)==False:
                    print(grafo.existe_nodo(desde), grafo.existe_nodo(hacia))
                    st.error("❗ Digita una ubicación y una dirección válidas.")
                else:
                    st.success(f"🔍 Buscando camino de '{desde}' a '{hacia}'.")
                    crear_grafo(grafo.get_trayecto(desde,hacia))
                    
    # Mostrar como tabla
    st.title("Cuadro de Ubicaciones")
    st.table(df1)
    # Mostrar como tabla
    st.title("Cuadro de Referencias")
    st.table(df2)

    





