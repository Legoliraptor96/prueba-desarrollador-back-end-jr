'''
Prueba para el puesto de desarrollador back end jr, Cura Deuda
Alonso Daniel Jacobo Hernández
'''
#Paquetes importados
from tkinter import N
import pandas as pd
import xlrd



#ignorar SettingWithCopyWarning 
pd.options.mode.chained_assignment = None  # default='warn'



#-----------------------Inicio Punto 2 --------------------------------------------------

#Ruta donde se encuentra el archivo
path=r"C:\Users\Alonso\Documents\GitHub\prueba-desarrollador-back-end-jr\CPdescarga.xls"

#Leer el archivo completo y guardarlo en una variable'
sepomex = pd.read_excel(path,sheet_name=None)

#Concatenar las hojas
df_sepomex=pd.concat(sepomex,ignore_index=True)


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



#-----------------------Inicio Punto 3 -----------------------------------------------

#generación de un data frame a partir del leido aleatorizando el orden de los datos en las columnas

df_sepomex_rand=df_sepomex.sample(frac=1).reset_index(drop=True)
#print(df_sepomex_rand)

#scrip que genera tablas a partir de data frames

'''
def script_rand(df_inp,repeticiones=None,df_out):
    df_out=[]
    for i in range(repeticiones):
        yield df_rand.sample(frac=1)
        #pd.concat(df_rand,names=["Replicas"])
'''


#Codigo para generar 10 veces la tabla con datos aleatorios Sepomex
'''
df_out=[]
count = 1
while (count < 11):
   df_out.append(df_sepomex.sample(frac=1).reset_index(drop=True))
   count = count + 1

pd.concat(df_out)

#print(df_out)
'''
#Codigo pasado a scrip generar n veces la tabla con datos aleatorios Sepomex

def script_rand(df_inp,df_out,n):
    #df_out=[]
    count = 1
    while (count <= n):
        df_out.append(df_inp.sample(frac=1).reset_index(drop=True))
        count = count + 1
    pd.concat(df_out)

df_rand=[]

script_rand(df_sepomex,df_rand,10)

print(df_rand)





