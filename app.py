"""
Proyecto - Machine Learning(conceptos) - Universidad de Cundinamarca - 601N
Modelo de prediccion para la insercion laboral de estudiantes de ingeniería en sistemas y computación
@author: Andres Rodriguez
@author: Jonathan Chavarro
"""
from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np 
from python.entrenar_modelo import make_prediction
from python.feedback import generate_feedback
from python.email import send_email

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
    feedback = None
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
            # Generar feedback personalizado
            feedback = generate_feedback(experience, skills, languages, result)

    return render_template("pages/model/modelo_predictivo.html", result=result, feedback=feedback)

@app.route("/enviar_feedback", methods=["POST"])
def enviar_feedback():
    try:
        # Obtener datos del formulario
        email = request.form.get('email')
        name = request.form.get('name')
        feedback = request.form.get('feedback')
        experience = request.form.get('experience')
        skills = request.form.get('skills')
        languages = request.form.get('languages')
        prediction = request.form.get('prediction')
        
        # Verificar datos requeridos
        if not all([email, name, feedback]):
            return jsonify({"success": False, "message": "Faltan datos requeridos"}), 400
        
        # Información del perfil para el correo
        profile_info = {
            "experience": experience,
            "skills": skills,
            "languages": languages,
            "prediction": "Sí" if prediction == "Sí" else "No"
        }
        
        # Enviar correo
        success = send_email(email, name, feedback, profile_info)
        
        if success:
            return jsonify({"success": True, "message": "Feedback enviado correctamente"})
        else:
            return jsonify({"success": False, "message": "Error al enviar el correo"}), 500
    
    except Exception as e:
        return jsonify({"success": False, "message": f"Error: {str(e)}"}), 500


@app.route("/enviar_contacto", methods=["POST"])
def enviar_contacto():
    try:
        email = request.form.get('email')
        nombre = request.form.get('nombre', '')
        mensaje = request.form.get('mensaje')
        
        if not all([email, mensaje]):
            return jsonify({"success": False, "message": "Faltan datos requeridos"}), 400
        
        from python.contacto import enviar_mensaje_contacto

        success = enviar_mensaje_contacto(email, nombre, mensaje)
        
        if success:
            return jsonify({"success": True, "message": "Mensaje enviado correctamente"})
        else:
            return jsonify({"success": False, "message": "Error al enviar el correo"}), 500
    
    except Exception as e:
        return jsonify({"success": False, "message": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
