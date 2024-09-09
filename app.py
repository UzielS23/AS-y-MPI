from flask import Flask

from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hola, Mundo!</p>"

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/alumnos/guardar", methods=["POST"])
def alumnosGuardar():
    matricula = request.form["txtmatriculaFA"]
    nombreapellido = request.form["txtNombreApellidoFA"]
    return f"matricula: {matricula} nombre y apellido : {nombreapellido}"

# app.run(debug=True, port=8000)