#python3 -m venv .env => crea una virtualizacion
#source .env/bin/activate => entra dentro de la virtualizacion
#deactivate => desactiva la virtualizacion
#pip install Flask => instala flask
#flask --app hello ru => metodo para correr la aplicacion desde flaske

from flask import Flask, jsonify
import json

import mysql.connector

cnx = mysql.connector.connect(
    user = "root", password ="admin@paradyse08",
    host="localhost",
    database="GraphicsCards",
    port="3306",
)

cursor = cnx.cursor()

cursor.execute("SELECT * FROM indice")
for (tecnologia, marca, modelo, release_year) in cursor:
    print("{} - {} {} ({})".format(tecnologia, marca, modelo, release_year))

data = cursor.fetchall()


app = Flask(__name__)

@app.route("/")
def main():
    return "SUG"

@app.route("/bye")
def adios():
    return "BYE SUG"

@app.route("/api/sql/test")
def apisql():
    cursor.execute("SELECT * FROM indice")
    data = []
    for row in cursor:
        data.append(row)
    return jsonify(data)

@app.route("/index")
def index():
    with open("index.json", "r") as f:
        index = json.load(f)
    return jsonify(index)

if __name__=='__main__':
    app.run()