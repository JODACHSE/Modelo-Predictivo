"""
Proyecto - Machine Learning(conceptos) - Universidad de Cundinamarca - 601N
Modelo de prediccion para la insercion laboral de estudiantes de ingeniería en sistemas y computación
@author: Andres Rodriguez
@author: Jonathan Chavarro
"""
from flask import Flask, render_template, request
import joblib
import numpy as np 
from python.entrenar_modelo import make_prediction

model = joblib.load('model/logreg_model.pkl')

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

# Conclusiones y Contacto
@app.route("/conclusiones")
def conclusiones():
    return render_template("pages/conclusiones.html")

@app.route("/contacto")
def contacto():
    return render_template("pages/contacto.html")


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


@app.route("/modelo_predictivo", methods=["GET", "POST"])
def modelo_predictivo():
    result = None
    if request.method == "POST":
        # Obtener los datos del formulario
        experience = request.form['years_of_experience']
        skills = request.form['soft_skills']
        languages = request.form['languages']
        
        # Verificar que las habilidades y los lenguajes no estén vacíos
        if not skills or not languages:
            result = "Por favor, selecciona al menos una habilidad y un lenguaje."
        else:
            # Realizar la predicción
            result = make_prediction(experience, skills, languages)

    return render_template("pages/model/modelo_predictivo.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
