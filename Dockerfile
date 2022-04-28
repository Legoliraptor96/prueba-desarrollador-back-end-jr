#Docker
#Prueba para el puesto de desarrollador back end jr, Cura Deuda
#Alonso Daniel Jacobo Hernández

FROM python:3.8

ADD ./prueba-desarrollador-backend-jr.py

RUN pip install pandas xlrd request

RUN pip install json

CMD [ "python","./prueba-desarrollador-backend-jr.py" ]
