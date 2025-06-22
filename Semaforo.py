class Semaforo:
    
    #tv = tiempo semaforo en verde 
    #tr = tiempo semaforo en rojo
    #c = cantidad de carros que pasan el semaforo sin que queden carros esperando
    #c = en caso de no haber semaforo se pone la cantidad de carros que pueden ocupar la calle
    #En caso se no haber un semaforo se toma el tiempo en verde y rojo como 1 para no afectar al peso de la arista
    def __init__(self, tv: int, tr: int, c: int):
        self.tv = tv
        self.tr = tr
        self.c = c