#python3 -m venv .env => crea una virtualizacion
#source .env/bin/activate => entra dentro de la virtualizacion
#deactivate => desactiva la virtualizacion
#pip install Flask => instala flask
#flask --app hello ru => metodo para correr la aplicacion desde flaske

from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "HOLA ITE"

@app.route("/bye")
def adios():
    return "BYE ITE"