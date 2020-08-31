import json

def leerJson():
    file = open('../REGISTROS/archivo1.json')
    datos = json.load(file)
    file.close()
    print(f'\n              Tipo de Estructura     -------->    {type(datos)}')
    print('\n')
    contador = 0
    for registro in datos:
        contador += 1
        print(f'     ({contador})    --    {registro}')



