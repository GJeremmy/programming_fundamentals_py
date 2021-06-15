class nodoSimple:
    def __init__(self, d=None):
        self.dato = d
        self.liga = None

    def asignarDato(self, d):
        self.dato = d

    def asignarLiga(self, x):
        self.liga = x

    def retornarDato(self):
        return self.dato

    def retornarLiga(self):
        return self.liga


class LSL:
    def __init__(self):  # Constructor
        self.primero = None
        self.ultimo = None

    def primerNodo(self):
        return self.primero

    def ultimoNodo(self):
        return self.ultimo

    def esVacia(self):
        return self.primero is None

    def finDeRecorrido(self, p):
        return p is None

    def recorrerLista(self):
        p = self.primerNodo()
        while not self.finDeRecorrido(p):
            print(p.retornarDato(), end=", ")
            p = p.retornarLiga()

    def agregarDato(self, d):
        x = nodoSimple(d)
        p = self.primerNodo()
        if p is None:
            self.primero = x
            self.ultimo = x
        else:
            self.ultimo.liga = x
            self.ultimo = x

    def buscarDondeInsertar(self, d):
        p = self.primerNodo()
        y = None
        while not self.finDeRecorrido(p) and p.retornarDato() < d:
            y = p
            p = p.retornarLiga()
        return y

    def insertar(self, d, y):
        x = nodoSimple(d)
        self.conectar(x, y)

    def conectar(self, x, y):
        if y is None:
            if self.primero is None:
                self.ultimo = x
            else:
                x.asignarLiga(self.primero)
            self.primero = x
            return
        x.asignarLiga(y.retornarLiga())
        y.asignarLiga(x)
        if y == self.ultimo:
            self.ultimo = x

    def longitud(self):
        p = self.primerNodo()
        n = 0
        while not self.finDeRecorrido(p):
            n = n + 1
            p = p.retornarLiga()
        return n

    def buscarDato(self, d, y):
        x = self.primerNodo()
        while not self.finDeRecorrido(x) and x.retornarDato() != d:
            y.asignarDato(x)
            x = x.retornarLiga()
        return x

    def borrar(self, x, y=None):
        if x is None:
            print("Dato no está en la lista")
            return
        if y is None:
            if x != self.primero:
                print("Falta el anterior del dato a borrar")
                return
        else:
            y = y.retornarDato()
        self.desconectar(x, y)

    def desconectar(self, x, y):
        if y is None:
            self.primero = x.retornarLiga()
            if self.esVacia():
                self.ultimo = None
        else:
            y.asignarLiga(x.retornarLiga())
            if x == self.ultimo:
                self.ultimo = y
