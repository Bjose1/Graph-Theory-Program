from Semaforo import Semaforo

class Nodo:
    
    #nombre = direccion en calle y carrera de la esquina
    #info = si tiene un semaforo de ahí se saca la informacion para sacar el peso de sus aristas adyacentes, es una lista con cada semaforo hacia cada esquina adyacente
    #nodos_ady_salida = las esquinas a las que puede llegar directamente
    #peso_aristas_salida = peso de distancia de esquina origen a la otra, se le da una lista con las distancia y los pesos se calculan
    #referencia = nombre de lugar entre las 2 esquinas que sirva como referencia
    def __init__(self, nombre: str, info: list, nodos_ady_salida: list, peso_aristas_salida: list, referencia : list):
        self.nombre = nombre
        self.info = info
        self.nodos_ady_salida = nodos_ady_salida
        self.peso_aristas_salida = self.calcular_peso(peso_aristas_salida)
        self.referencia = referencia
        
    #dist = Distancias de nodo a todos sus nodos adyacentes
    def calcular_peso(self, dist: list) -> list:
        if len(dist) > 1:
            for i in range(len(dist)):
                dist[i] = int(float(dist[i]/10 * (((self.info[i].tr)/(4*self.info[i].tv))) + self.info[i].c))
                if dist[i] >= 1000:
                    dist[i] = int(dist[i]/100)
        elif len(dist) == 0:
            return dist
        else:
            i = 0
            dist[i] = int(float(dist[i]) * float((self.info[i].tr/self.info[i].tv) * (self.info[i].c)))
            if dist[i] >= 1000:
                    dist[i] = int(dist[i]/100)
        return dist
    
    
    """def calcular_peso(self, dist: list) -> list:
        if len(dist) > 1:
            for i in range(len(dist)):
                dist[i] = int(float(dist[i] * ((self.info[i].tr/self.info[i].tv*2) * (self.info[i].c)))/30)
                if(dist[i] > 1000):
                    dist[i] = int(dist[i]/10)
        elif len(dist) == 0:
            return dist
        else:
            i = 0
            dist[i] = int(float(dist[i]) * float((self.info[i].tr/self.info[i].tv) * (self.info[i].c)))
            if(dist[i] > 1000):
                    dist[i] = int(dist[i]/10)
        return dist"""""