"""
Proyecto - Machine Learning - Universidad de Cundinamarca - 601N
Modelo de prediccion para lla insercion laboral de estudiantes de ingenieria en sistemas y computacion
@author: Andres Rodriguez
@author: Jonathan Chavarro
"""
from flask import Flask, render_template

app = Flask(__name__)

app.config["DEBUG"] = True
app.config["ENV"] = "development"


@app.route("/")
def home():
    return render_template("home.html")

# Paginas de presentation
@app.route("/objetivos")
def objetivos():
    return render_template("pages/presentation/objetivos.html")


@app.route("/metodologia")
def metodologia():
    return render_template("pages/presentation/metodologia.html")


@app.route("/conclusiones")
def conclusiones():
    return render_template("pages/presentation/conclusiones.html")


@app.route("/contacto")
def contacto():
    return render_template("pages/presentation/contacto.html")


# Paginas de model
@app.route("/por_que")
def por_que():
    return render_template("pages/model/por_que.html")


@app.route("/como_funciona")
def como_funciona():
    return render_template("pages/model/como_funciona.html")


@app.route("/dataset")
def dataset():
    return render_template("pages/model/dataset.html")


@app.route("/entrenamiento")
def entrenamiento():
    return render_template("pages/model/entrenamiento.html")


@app.route("/modelo_predictivo")
def modelo_predictivo():
    return render_template("pages/model/modelo_predictivo.html")


if __name__ == "__main__":
    app.run(debug=True)
