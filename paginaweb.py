'''
Prueba para el puesto de desarrollador back end jr, Cura Deuda
Alonso Daniel Jacobo Hernández
pagina web
'''

from flask import Flask, render_template

app = Flask(__name__,template_folder='templates')

@app.route('/')
def principal():
    return render_template('index.html')


if __name__ == '__main__':
    #Pagina web en modo debug para trabajr comodamente
 app.run(debug=True)


