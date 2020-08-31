from xml.etree.ElementTree import parse


def cargaXml():
    datos = parse('../REGISTROS/archivo2.xml')

    contador = 0
    print(f'\n              Tipo de Estructura     -------->    {type(datos)}        ---------> árbol = tree')
    print('\n')
    print('\nNo      Nombre               Apellido             Edad    Ciudad')
    for registro in datos.iterfind('persona'):
        contador += 1
        print(f'''({contador})     {registro.findtext('nombres')}        {registro.findtext('apellidos')}       {registro.findtext('edad')}      {registro.findtext('ciudad')}''')
