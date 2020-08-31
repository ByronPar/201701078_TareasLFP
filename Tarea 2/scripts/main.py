import os
import sys

from scripts import cargaArchivo1, cargaArchivo2, cargaArchivo3


def quit():
    print("\n FIN DE LA APLICACIÓN  ")
    sys.exit(0)


def mostrar_menu():
    print("""
    #########################      Menu Principal      #########################
                        1)   Cargar Archivo 1   ---   .json
                        2)   Cargar Archivo 2   ---   .xml
                        3)   Cargar Archivo 3   ---   .csv
                        4)   Salir
    """)


class Menu:
    def __init__(self):
        self.elecciones = {  # mi diccionario menu
            "1": self.archivo1,
            "2": self.archivo2,
            "3": self.archivo3,
            "4": quit
        }

    def run(self):  # Para Correr mi menu
        while True:
            mostrar_menu()
            eleccion = input("\n   Seleccione una opción: ")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
                break
            else:
                os.system("cls")
                print("\n{0} no es una elección válida".format(eleccion))

    def archivo1(self):
        cargaArchivo1.leerJson()
        self.run()

    def archivo2(self):
        cargaArchivo2.cargaXml()
        self.run()

    def archivo3(self):
        cargaArchivo3.cargaCsv()
        self.run()


if __name__ == '__main__':
    Menu().run()
