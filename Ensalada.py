from Fruta import Fruta

class Ensalada:
    
    tamano = 0
    ingredientes = []
    crema = False
    nombre = ''
    
    def __init__(self, nombre, tamano, ingredientes, crema):
        self.tamano = tamano
        self.ingredientes = ingredientes
        self.crema = crema
        self.nombre = nombre