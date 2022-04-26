'''
Prueba para el puesto de desarrollador back end jr, Cura Deuda
Alonso Daniel Jacobo Hernández
'''
#Paquetes importados
import pandas as pd
import xlrd

#Ruta donde se encuentra el archivo
path=r"C:\Users\Alonso\Documents\GitHub\prueba-desarrollador-back-end-jr\CPdescarga.xls"

#Leer el archivo completo y guardarlo en una variable'
SEPOMEX = pd.read_excel(path,sheet_name=None)

#Concatenar las hojas
df_sepomex=pd.concat(SEPOMEX,ignore_index=True)

#Prueba imprimir tablas concatenadas
#print(df_sepomex)

df_estado=df_sepomex[['d_codigo','c_estado']]

#Prueba imprimir tabla de Codigo vs Estado
df_estado.rename({'d_codigo': 'Codigo'}, axis=1, inplace=True)
df_estado.rename({'c_estado': 'Estado'}, axis=1, inplace=True)

#Prueba imprimir tabla de Codigo vs Estado
#print(df_estado)

df_municipio=df_sepomex[['d_codigo','D_mnpio']]

#Prueba imprimir tabla de Codigo vs Municpio
df_municipio.rename({'d_codigo': 'Codigo'}, axis=1, inplace=True)
df_municipio.rename({'D_mnpio': 'Municipio'}, axis=1, inplace=True)

#Prueba imprimir tabla de Codigo vs Municpio
#print(df_municipio)

df_ciudad=df_sepomex[['d_codigo','d_ciudad']]

#Prueba imprimir tabla de Codigo vs Municpio
df_ciudad.rename({'d_codigo': 'Codigo'}, axis=1, inplace=True)
df_ciudad.rename({'d_ciudad': 'Ciudad'}, axis=1, inplace=True)

#Prueba imprimir tabla de Codigo vs Municpio
#print(df_municipio)




'''Apertura del archivo SEPOMEX, en modo lectura para evitar modificaciones

#SEPOMEX = open("CPdescarga.txt",mode="r")

 df = pd.read_csv('CPdescarga.txt', sep='|')

#print(SEPOMEX.read())
'''

'''
with open("CPdescarga.txt") as SEPOMEX:
    data = f.readlines()[2:100000]
print(data)
'''
'''
with open("CPdescarga.txt") as SEPOMEX:
    next(SEPOMEX)  # Descartar la primera línea
    next(SEPOMEX)  # Descartar la Segundo línea
    for linea in SEPOMEX:
        print(linea)
'''


