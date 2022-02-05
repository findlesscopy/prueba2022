from nodo import Nodo

class ListaDoblementeEnlazada():
    
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def vacia(self):
        return self.primero == None
    
    def agregar_final(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
    
    def agregar_inicio(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
    
    def recorrer_inicio(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
    
    def recorrer_final(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior

    def eliminar_inicio(self):
        if self.vacia():
            print("Está vacía")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
    
    def eliminar_final(self):
        if self.vacia():
            print("Está vacía")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None