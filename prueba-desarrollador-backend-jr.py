'''
Prueba para el puesto de desarrollador back end jr, Cura Deuda
Alonso Daniel Jacobo Hernández
'''
#Paquetes importados
from pprint import pprint
from tkinter import N
from urllib import response
import pandas as pd
import xlrd
import json
import requests


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
    count = 1
    while (count <= n):
        df_out.append(df_inp.sample(frac=1).reset_index(drop=True))
        count = count + 1
    pd.concat(df_out)
    

df_rand=[]


script_rand(df_sepomex,df_rand,10)

#print(df_rand)


#-----------------------Fin Punto 3 -----------------------------------------------

#-----------------------Inicio Punto 4 y 5-----------------------------------------------

#generar un archivo json a partir de aleatorizacion de lo datos de SEPOMEX


diccionario={}

def script_rand_tojs(df_inp,diccionario,n):
    count = 1
    while (count <= n):
        count = count + 1
        rand =df_inp.sample(frac=1).reset_index(drop=True)
        diccionario=rand.to_json(orient = 'columns')
        with open('./sepomex.json', 'w') as file:json.dump(diccionario, file,sort_keys=True, indent=4)
    

script_rand_tojs(df_sepomex,diccionario,10)

#abrimos de nuevo el json generado y asignamos a una variable

with open('./sepomex.json',"r") as sepomexjs:
    #pasamos el json a  diccionario
    json_diccionario = json.load(sepomexjs)

#pprint(#pasamos el json a  diccionario)

#nueva entrada a agregar

def nuevaentrada(d_codigo,d_asenta,d_tipo_asenta,D_mnpio,d_estado,d_ciudad,d_CP,c_estado,c_oficina,c_CP,c_tipo_asenta,c_mnpio,id_asenta_cpcons,d_zona,c_cve_ciudad):
    entrada={d_codigo,d_asenta,d_tipo_asenta,D_mnpio,d_estado,d_ciudad,d_CP,c_estado,c_oficina,c_CP,c_tipo_asenta,c_mnpio,id_asenta_cpcons,d_zona,c_cve_ciudad}
    json_diccionario.append(entrada)

#-----------------------Fin Punto 4 y 5-----------------------------------------------

#-----------------------inicio parte 7-----------------------------------------------

#capa de seguridad mediante HTTPBasicAuth, comentada por motivos de comodidad

'''
from requests.auth import HTTPBasicAuth
response = requests.get('pagina web de interes ejemplo github',auth=HTTPBasicAuth('usuario','contraseña'))
response = requests.get('https://api.github.com/user',auth=HTTPBasicAuth('usuario','contraseña'))
print('Codigo de respuesta'+ str(response.status_code))
if response.status_code == 200
    print('Acesso correctamente: '+response.text)
'''
#-----------------------Fin parte 7-----------------------------------------------


#intentos implementacion de busqueda parte 4 y 5, por motivos de tiempo ya no pude hacer mas pruebas 
#pero dejo como evidencia las ideas que tenia

#print(list(filter(lambda x:x['d_CP']==string,json_diccionario)))

'''
def jsoncp(json, cp):
    for item in json['d_CP']:
        if item['d_CP'] == cp:
            return item['d_asenta']
        

jsoncp(json_diccionario,20001)
'''
'''
for entry in json_diccionario:
    if '20001' == json_diccionario['d_CP']
    print( 'el codigo postal'    , ' colonia  :', json_diccionario['d_asenta'])
'''

'''
def jsoncp (cp):
    for entry in js:
        if cp == entry['d_CP']:
            print(entry['d_asenta'])

jsoncp('20001')
'''
'''
i=0
item=20001
for item in js_obj['d_CP']:
    if item in js_obj['d_CP'] :
        i=i+1
print(i)
 '''   

'''
def jsoncp(json, cp):
    for item in json['d_CP']:
        if item['d_CP'] == cp:
            return item['d_asenta']
        
'''

'''
def jsoncp (cp):
    for entry in js:
        if cp == entry ['d_CP']:
            return entry ['d_asenta']
        
jsoncp(20001)
'''

'''
for item in js:
    print item['d_codigo']
    print item['d_asenta']
'''












