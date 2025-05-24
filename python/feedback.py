import os
from dotenv import load_dotenv
import google.generativeai as genai

# Cargar variables de entorno
load_dotenv()

# Configurar la API de Google Generative AI
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

def generate_feedback(experience, skills, languages, result):
    """
    Genera feedback personalizado basado en el perfil del usuario y el resultado de la predicción
    """
    try:
        # Verificar si tenemos una API key configurada
        if not API_KEY:
            return generate_fallback_feedback(experience, skills, languages, result)
        
        # Configurar el modelo - Gemini Pro es el modelo recomendado actualmente
        model = genai.GenerativeModel('gemini-pro')
        
        # Crear el prompt para el modelo
        prompt = f"""
        Como experto en recursos humanos y empleabilidad en el sector tecnológico, proporciona un feedback personalizado 
        para un ingeniero de sistemas con el siguiente perfil:
        
        - Años de experiencia: {experience}
        - Habilidades blandas: {skills}
        - Lenguajes de programación: {languages}
        
        Según nuestro modelo predictivo, este perfil {'' if result == 'Sí' else 'NO'} tiene buenas posibilidades de conseguir empleo.
        
        Por favor, proporciona:
        1. Un análisis breve de las fortalezas del perfil
        2. Áreas de mejora específicas
        3. Recomendaciones concretas para aumentar su empleabilidad
        4. Tendencias actuales del mercado laboral relevantes para este perfil
        
        El feedback debe ser constructivo, específico y orientado a la acción.
        """
        
        # Generar respuesta
        response = model.generate_content(prompt)
        
        # Devolver el texto generado
        return response.text
    
    except Exception as e:
        print(f"Error al generar feedback con IA: {str(e)}")
        return generate_fallback_feedback(experience, skills, languages, result)

def generate_fallback_feedback(experience, skills, languages, result):
    """
    Genera un feedback básico cuando la IA no está disponible
    """
    # Convertir experiencia a número
    try:
        exp_years = int(experience)
    except:
        exp_years = 0
    
    # Contar habilidades y lenguajes
    skill_count = len(skills.split(',')) if skills else 0
    lang_count = len(languages.split(',')) if languages else 0
    
    # Feedback básico
    if result == 'Sí':
        return f"""
        ¡Buenas noticias! Tu perfil muestra potencial para conseguir empleo en el sector tecnológico.
        
        Fortalezas:
        - Cuentas con {exp_years} años de experiencia, lo cual es valioso.
        - Conoces {lang_count} lenguajes de programación: {languages}.
        - Has desarrollado {skill_count} habilidades blandas importantes: {skills}.
        
        Recomendaciones:
        - Continúa ampliando tu portafolio con proyectos prácticos.
        - Considera obtener certificaciones en los lenguajes que dominas.
        - Participa en comunidades tecnológicas para expandir tu red profesional.
        """
    else:
        return f"""
        Según nuestro análisis, tu perfil actual podría beneficiarse de algunas mejoras para aumentar tus posibilidades de empleabilidad.
        
        Áreas de mejora:
        - Experiencia: {exp_years} años podrían no ser suficientes para algunos roles. Considera proyectos freelance o voluntariado.
        - Lenguajes de programación: Conoces {languages}. Considera aprender lenguajes con alta demanda como Python, JavaScript o Java.
        - Habilidades blandas: Has mencionado {skills}. Trabaja en desarrollar habilidades como resolución de problemas y comunicación efectiva.
        
        Recomendaciones:
        - Realiza cursos online para ampliar tus conocimientos técnicos.
        - Desarrolla proyectos personales para demostrar tus habilidades.
        - Participa en hackathons o eventos de networking del sector.
        """