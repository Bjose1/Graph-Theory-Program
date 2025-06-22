from Semaforo import Semaforo
from Nodo import Nodo
from ColaPrioridad import ColaPrioridad

class Grafo:
    
    #nodos = lista con los objetos nodo
    #ady = diccionario con clave: valor -> nodo(objeto): nodos adyacentes
    #Al agregar un nodo al grafo se agrega a la lista y al diccionario 
    #pesos = diccionario clave : valor -> nodo(objeto): pesos de aristas hacia nodos adyacentes
    #referencia = diccionario clave : valor -> nodo(objeto) = lugar al que se llegar
    def __init__(self, nodos: list, ady: dict, pesos: dict, referencia: dict):
        self.nodos = nodos
        self.ady = ady
        self.pesos = pesos
        self.referencia = referencia
    
    def __init__(self):
        self.nodos = list()
        self.ady = dict()
        self.pesos = dict()
        self.referencia = dict()
        
    def agregar_nodo(self, nodo: Nodo):
        self.nodos.append(nodo)        
        self.ady.update({nodo: nodo.nodos_ady_salida})
        self.pesos.update({nodo: nodo.peso_aristas_salida})
        self.referencia.update({nodo: nodo.referencia})
    
    
    def dijkstra(self,inicio: Nodo):
        distancia = dict()
        padre = dict()
        visto = set()
        cola_prioridad = ColaPrioridad()
        for nodo in self.nodos:
            distancia[nodo] = float("inf")
            padre[nodo] = None
        
        distancia[inicio] = 0
        cola_prioridad.add(inicio,0)
        while not cola_prioridad.vacia():
            #u = nodo actual
            u = cola_prioridad.pop()
            if u not in visto:
                visto.add(u)
                i = 0
                #Se recorren los vecinos (vecino es str pero con get_nodo se convierten en nodo)
                for vecino in self.ady[u]:
                    v = self.get_nodo(vecino)
                    peso_uv = self.pesos[u][i]
                    nueva_dist = distancia[u] + peso_uv
                    if nueva_dist < distancia[v]:
                        distancia[v] = nueva_dist
                        padre[v] = u
                        cola_prioridad.add(v, nueva_dist)
        
        return distancia, padre
            
    def get_nodo(self, nombre: str):
        for nodo in self.nodos:
            if nodo.nombre == nombre:
                return nodo
    
    def get_menor_distancia(self, inicio: str, destino: str):
        distancia, padre = self.dijkstra(self.get_nodo(inicio))
        return distancia[destino]
    
    def get_trayecto(self, inicio: str, destino: str):
        distancia, padre = self.dijkstra(self.get_nodo(inicio))
        pivot = self.get_nodo(destino)
        camino_reves = list()
        camino_reves.append(pivot.nombre)
        while padre[pivot] != None:
            pivot = padre[pivot]
            camino_reves.append(pivot.nombre)
        camino_reves.reverse()
        referencias = list()
        calle = self.get_nodo(camino_reves[0])
        for i in range(len(camino_reves) - 1):
            calle = self.get_nodo(camino_reves[i])
            for j in range(len(calle.nodos_ady_salida)):
                if calle.nodos_ady_salida[j] == camino_reves[i+1]:
                    referencias.append(calle.referencia[j])
            print("Aqui")
            print(referencias)

        """if len(camino_reves) >1:
            for calle in camino_reves:
                calle = self.get_nodo(calle)
                if(i <= len(camino_reves) - 1):
                    for ady in calle.nodos_ady_salida:
                        if ady == camino_reves[i+1]:
                            referencias.append(calle.referencia[i])
                i+=1"""



        return referencias
            
    def trayecto_referencia(self, inicio : str, destino: str):
        for nodo in self.nodos:
            for referencia in nodo.referencia:
                if inicio == referencia:
                    calle_inicio = nodo
                if destino == referencia:
                    calle_destino = nodo
        return self.get_trayecto(calle_inicio.nombre, calle_destino.nombre)
        
        
                
        
    def get_referencias(self, direccion: Nodo):
        return self.referencia[direccion]
        
    def get_referencia(self, direccion1: Nodo, direccion2: Nodo):
        # Verifica si los nodos existen en self.ady
        nodo1 = self.get_nodo(direccion1)
        nodo2 = self.get_nodo(direccion2)
        
        if nodo1 not in self.ady or nodo2 not in self.ady:
            return None

        # Busca direccion2 en las adyacencias de direccion1
        for i in range(len(self.ady[nodo1])):
            if self.ady[nodo1][i] == nodo2.nombre:
                return self.referencia[nodo1][i]  # Retorna la referencia si existe
        
        # Si no se encontró, busca en sentido inverso (sin recursión)
        for i in range(len(self.ady[nodo2])):
            if self.ady[nodo2][i] == nodo1:
                return self.referencia[nodo2][i]

    
    def mostrar_adyacencias(self):
        for nodo in self.ady:
            print(nodo.nombre + "  ->  " + str(nodo.nodos_ady_salida))
    
    def mostrar_referencias(self):
        for nodo in self.referencia:
            print(nodo.nombre + "  ->  " + str(nodo.referencia))
    
    def mostrar_pesos(self, nodo: str):
        nodo = self.get_nodo(nodo)
        print(nodo.nombre)
        for peso in  nodo.peso_aristas_salida:
            print(peso)
    
    def existe_nodo(self, direccion: str) -> bool:
        for nodo in self.nodos:
            if nodo.nombre == direccion:
                return True
        return False
    
    def pesos(self):
        for nodo in self.nodos:
            for peso in nodo.peso_aristas_salida:
                print(peso)
        