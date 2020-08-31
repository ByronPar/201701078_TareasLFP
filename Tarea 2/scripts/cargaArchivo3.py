import pandas as pd

def cargaCsv():
    df = pd.read_csv('../REGISTROS/archivo3.csv', sep='$')
    print(f'\n              Tipo de Estructura     -------->    {type(df)}     ----   Es un DataFrame')
    print('\n')
    print(df)


