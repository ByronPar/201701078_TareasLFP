LISTAOBJETOS = []


class Dato:
    def __init__(self, nombre, edad, activo, saldo):
        self.__nombre = nombre
        self.__edad = edad
        self.__activo = activo
        self.__saldo = saldo

    #metodos del objeto

    #getter and setters
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, new_edad):
        self.__edad = new_edad

    @property
    def activo(self):
        return self.__activo

    @activo.setter
    def activo(self, new_activo):
        self.__activo = new_activo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, new_saldo):
        self.__saldo = new_saldo
