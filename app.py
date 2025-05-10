"""
Proyecto - Machine Learning(conceptos) - Universidad de Cundinamarca - 601N
Modelo de prediccion para la insercion laboral de estudiantes de ingeniería en sistemas y computación
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

# Entendimiento del negocio y de los datos
@app.route("/entendimiento")
def entendimiento():
    return render_template("pages/presentation/entendimiento.html")

# Ingeniería de datos
@app.route("/ingenieria-datos")
def ing_datos():
    return render_template("pages/presentation/ing_datos.html")

# Ingeniería del modelo
@app.route("/ingenieria-modelo")
def ing_modelo():
    return render_template("pages/presentation/ing_modelo.html")

# Modelo Predictivo
@app.route("/modelo-predictivo")
def modelo_predictivo():
    return render_template("pages/model/modelo_predictivo.html")

# Conclusiones y Contacto
@app.route("/conclusiones")
def conclusiones():
    return render_template("pages/conclusiones.html")

@app.route("/contacto")
def contacto():
    return render_template("pages/contacto.html")

if __name__ == "__main__":
    app.run(debug=True)
