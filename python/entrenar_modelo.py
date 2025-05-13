import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression

# Cargar el modelo previamente entrenado
model = joblib.load('model/logreg_model.pkl')

# Funciones auxiliares que utilizas en el preprocesamiento
def extract_experience(qualifications):
    if isinstance(qualifications, str) and 'year' in qualifications.lower():
        years = [int(s) for s in qualifications.split() if s.isdigit()]
        return years[0] if years else 0
    return 0

def count_skills(text):
    skills_keywords = ['management', 'design', 'analysis', 'development', 'engineering', 'programming']
    if isinstance(text, str):
        return sum(keyword.lower() in text.lower() for keyword in skills_keywords)
    return 0

def count_programming_languages(text):
    programming_languages = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby', 'C#', 'PHP', 'Swift', 'Go', 'Kotlin']
    if isinstance(text, str):
        return sum(language.lower() in text.lower() for language in programming_languages)
    return 0

# Función para hacer la predicción
def make_prediction(experience, skills, programming_languages):
    # Contar las habilidades y lenguajes de programación
    skills_count = count_skills(skills)
    programming_count = count_programming_languages(programming_languages)
    
    # Convertir la experiencia del usuario en el formato adecuado
    years_of_experience = extract_experience(experience)
    
    # Crear las características del modelo
    X_user = np.array([[years_of_experience, skills_count, programming_count]])
    
    # Hacer la predicción con el modelo
    prediction = model.predict(X_user)
    
    return "Sí" if prediction == 1 else "No"

# Ejemplo de uso
user_experience = "3 years of experience in software development"
user_skills = "management, development, programming"
user_languages = "Python, Java, C++"

prediction = make_prediction(user_experience, user_skills, user_languages)
print(f"¿Puede ser contratado? {prediction}")
