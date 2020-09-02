import webbrowser

from almacenamiento import LISTAOBJETOS


def crearReporte():
    f = open('reporte.html', 'w')
    contenido = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Reporte Html - Python</title>
  </head>
  <style type="text/css">
    table,
    th,
    td {
      border: 1px solid black;
      border-collapse: collapse;
    }
    th,
    td {
      padding: 10px;
    }
    th {
      text-align: center;
    }
    table {
      width: 100%;
      background-color: #f3f387;
    }
  </style>
  <body>
  <center><strong><h1>Reporte-Html     Carnet: 201701078    Nombre: Byron Josue Par Rancho</h1></strong></center>
  <hr/>
    <table>
      <tr >
      <th>
           No.
        </th>
        <th>
          Nombre
        </th>
        <th>
          Edad
        </th>
        <th>
          Activo
        </th>
        <th>
          Saldo
        </th>
      </tr>"""
    contador = 0
    for dato in LISTAOBJETOS:
        contador += 1
        contenido += f""" 
         <tr>
<td>
          {contador}
        </td>
        <td>
          {dato.nombre}
        </td>
        <td>
          {dato.edad}
        </td>
        <td>
          {dato.activo}
        </td>
        <td>
          {dato.saldo}
        </td>
      </tr>  """
    contenido += """</table>
  </body>
</html>"""

    f.write(str(contenido))
    f.close()
    webbrowser.open(
        'reporte.html'
    )