"""
Proyecto - Machine Learning - Universidad de Cundinamarca - 601N
Modelo de prediccion para lla insercion laboral de estudiantes de ingenieria en sistemas y computacion
@author: Andres Rodriguez
@author: Jonathan Chavarro
"""
from flask import Flask, render_template, request
import joblib
import numpy as np 
model = joblib.load('model/logreg_model.pkl')

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


# Preprocesamiento de los datos
def preprocess_input(experience, skills, languages):
    # Función para extraer años de experiencia
    def extract_experience(qualifications):
        if isinstance(qualifications, str) and 'year' in qualifications.lower():
            years = [int(s) for s in qualifications.split() if s.isdigit()]
            return years[0] if years else 0
        return 0

    # Función para contar las habilidades
    def count_skills(text):
        skills_keywords = ['management', 'design', 'analysis', 'development', 'engineering', 'programming']
        if isinstance(text, str):
            return sum(keyword.lower() in text.lower() for keyword in skills_keywords)
        return 0

    # Función para contar lenguajes de programación
    def count_programming_languages(text):
        programming_languages = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby', 'C#', 'PHP', 'Swift', 'Go', 'Kotlin']
        if isinstance(text, str):
            return sum(language.lower() in text.lower() for language in programming_languages)
        return 0

    # Contar las habilidades y lenguajes de programación
    skills_count = count_skills(skills)
    programming_count = count_programming_languages(languages)

    # Convertir la experiencia del usuario en el formato adecuado
    years_of_experience = extract_experience(experience)

    # Crear el vector de entrada
    input_data = np.array([[years_of_experience, skills_count, programming_count]])

    return input_data


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
