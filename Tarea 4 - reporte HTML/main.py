from almacenamiento import LISTAOBJETOS, Dato
from reporte import crearReporte
if __name__ == '__main__':
    #enlisto 15 objetos en una lista
    LISTAOBJETOS.append(Dato('Byron',12,500.25,4000.50))
    LISTAOBJETOS.append(Dato('Carlos',15,450.21,5000.00))
    LISTAOBJETOS.append(Dato('Roberto',21,516.25,1500.00))
    LISTAOBJETOS.append(Dato('Carol',25,12.5,300.00))
    LISTAOBJETOS.append(Dato('Mauricio',45,600.00,75000.25))

    LISTAOBJETOS.append(Dato('Muriel', 22, 540.25, 1000.50))
    LISTAOBJETOS.append(Dato('Johanna', 19, 315.45, 500.00))
    LISTAOBJETOS.append(Dato('Andrea', 24, 215.25, 10000.00))
    LISTAOBJETOS.append(Dato('Estuardo', 18, 250.26, 3000.00))
    LISTAOBJETOS.append(Dato('Marta', 55, 6000.00, 85000.25))

    LISTAOBJETOS.append(Dato('Heidy', 21, 45.45, 351.15))
    LISTAOBJETOS.append(Dato('Mauro', 23, 561.00, 4512.15))
    LISTAOBJETOS.append(Dato('Vivian', 19, 4892.00, 15000.00))
    LISTAOBJETOS.append(Dato('Paola', 31, 458.15, 10000.00))
    LISTAOBJETOS.append(Dato('Jaime', 75, 755.15, 7400.25))
    #ejecuto el metodo que correra mi html

    crearReporte()
