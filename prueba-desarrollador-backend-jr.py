'''
Prueba para el puesto de desarrollador back end jr, Cura Deuda
Alonso Daniel Jacobo Hernández
'''
#Paquetes importados
import pandas as pd
import xlrd



#ignorar SettingWithCopyWarning 
pd.options.mode.chained_assignment = None  # default='warn'



#-----------------------Inicio Punto 2 --------------------------------------------------

#Ruta donde se encuentra el archivo
path=r"C:\Users\Alonso\Documents\GitHub\prueba-desarrollador-back-end-jr\CPdescarga.xls"

#Leer el archivo completo y guardarlo en una variable'
SEPOMEX = pd.read_excel(path,sheet_name=None)

#Concatenar las hojas
df_sepomex=pd.concat(SEPOMEX,ignore_index=True)

#Prueba imprimir tablas concatenadas
#print(df_sepomex)

df_estado=df_sepomex[['d_codigo','d_estado']]

#Prueba imprimir tabla de Codigo vs Estado
df_estado.rename({'d_codigo': 'Codigo'}, axis=1, inplace=True)
df_estado.rename({'d_estado': 'Estado'}, axis=1, inplace=True)

#Prueba imprimir tabla de Codigo vs Estado
#print(df_estado)

df_municipio=df_sepomex[['d_codigo','D_mnpio']]

#Prueba imprimir tabla de Codigo vs Municpio
df_municipio.rename({'d_codigo': 'Codigo'}, axis=1, inplace=True)
df_municipio.rename({'D_mnpio': 'Municipio'}, axis=1, inplace=True)

#Prueba imprimir tabla de Codigo vs Ciudad
#print(df_municipio)

df_ciudad=df_sepomex[['d_codigo','d_ciudad']]

#Prueba imprimir tabla de Codigo vs Ciudad
df_ciudad.rename({'d_codigo': 'Codigo'}, axis=1, inplace=True)
df_ciudad.rename({'d_ciudad': 'Ciudad'}, axis=1, inplace=True)

#Prueba imprimir tabla de Codigo vs Ciudad
#print(df_ciudad)

#union de las 3 tablas 
df_tablas=[df_estado,df_municipio,df_ciudad]
df_union=pd.concat(df_tablas)

#Prueba imprimir concatenacion de tablas
#print(df_union)

#-----------------------Fin Punto 2 --------------------------------------------------



