import heapq

class ColaPrioridad():

    def __init__(self):
        """Inicializa una cola de prioridad vacía."""
        self._elementos = []
        self._indice = 0  # Para evitar comparaciones entre elementos iguales
    
    def add(self, elemento, prioridad: float):
        heapq.heappush(self._elementos, (prioridad, self._indice, elemento))
        self._indice += 1
        
    def pop(self):
        if self.vacia():
            raise IndexError("La cola de prioridad está vacía.")
        return heapq.heappop(self._elementos)[-1]  # Retorna solo el elemento

    def vacia(self) -> bool:
        """Verifica si la cola está vacía."""
        return len(self._elementos) == 0