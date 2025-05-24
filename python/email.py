import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv
import pathlib

load_dotenv()

def send_email(recipient_email, name, feedback, profile_info):
    """
    Envía un correo electrónico con el feedback generado por Gemini.
    
    Args:
        recipient_email (str): Correo electrónico del destinatario
        name (str): Nombre del destinatario
        feedback (str): Feedback generado por Gemini
        profile_info (dict): Información del perfil del usuario
    
    Returns:
        bool: True si el correo se envió correctamente, False en caso contrario
    """
    try:
        # Configuración del servidor SMTP para Gmail
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = os.environ.get("EMAIL_USER")
        password = os.environ.get("EMAIL_PASSWORD")
        
        if not sender_email or not password:
            print("Error: Credenciales de correo no configuradas en el archivo .env")
            return False
        
        # Crear mensaje
        message = MIMEMultipart("related")
        message["Subject"] = "Tu Feedback Personalizado - Modelo Predictivo de Empleabilidad"
        message["From"] = sender_email
        message["To"] = recipient_email
        
        # Parte alternativa para clientes que no pueden ver HTML
        msgAlternative = MIMEMultipart('alternative')
        message.attach(msgAlternative)
        
        # Determinar si la predicción es positiva o negativa para personalizar el mensaje
        es_positivo = profile_info.get('prediction', '').lower() == 'sí'
        
        # Crear versión HTML del mensaje
        html = f"""
        <html>
        <head>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700&display=swap');
                
                body {{
                    font-family: 'Roboto', Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    background-color: #f5f5f5;
                    margin: 0;
                    padding: 0;
                }}
                
                .container {{
                    max-width: 650px;
                    margin: 0 auto;
                    background-color: #ffffff;
                    border-radius: 8px;
                    overflow: hidden;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                }}
                
                .header {{
                    background-color: #4a6fdc;
                    color: white;
                    padding: 25px;
                    text-align: center;
                    position: relative;
                }}
                
                .header h1 {{
                    margin: 0;
                    font-size: 28px;
                    font-weight: 700;
                    letter-spacing: 0.5px;
                }}
                
                .logo-container {{
                    text-align: center;
                    padding: 15px;
                    background-color: #ffffff;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    width: 100%;
                }}
                
                .logo {{
                    max-width: 50px;
                    height: auto;
                    margin-right: 0; /* Eliminado el margen derecho */
                }}
                
                .brand-text {{
                    font-family: 'Cinzel Decorative', cursive;
                    font-weight: 700;
                    font-size: 24px;
                    color: #212529;
                    margin-left: 10px; /* Añadido margen izquierdo para separar del logo */
                }}
                
                .content {{
                    padding: 30px;
                    background-color: #ffffff;
                }}
                
                .greeting {{
                    font-size: 18px;
                    font-weight: 500;
                    margin-bottom: 20px;
                }}
                
                .profile {{
                    background-color: #f0f4f8;
                    padding: 20px;
                    margin-bottom: 25px;
                    border-radius: 8px;
                    border-left: 5px solid #4a6fdc;
                }}
                
                .profile h3 {{
                    margin-top: 0;
                    color: #2c3e50;
                    font-size: 20px;
                }}
                
                .profile ul {{
                    padding-left: 20px;
                }}
                
                .profile li {{
                    margin-bottom: 8px;
                }}
                
                .analysis {{
                    background-color: #ffffff;
                    padding: 0 10px;
                    margin-bottom: 25px;
                    border-radius: 8px;
                }}
                
                .analysis h3 {{
                    color: #2c3e50;
                    font-size: 20px;
                    border-bottom: 2px solid #eaeaea;
                    padding-bottom: 10px;
                }}
                
                .feedback-content {{
                    white-space: pre-line;
                    line-height: 1.8;
                }}
                
                .prediction-badge {{
                    display: inline-block;
                    padding: 6px 12px;
                    border-radius: 20px;
                    font-weight: bold;
                    color: white;
                    background-color: {es_positivo and '#28a745' or '#dc3545'};
                }}
                
                .recommendations {{
                    margin-top: 25px;
                }}
                
                .recommendations ul {{
                    padding-left: 20px;
                }}
                
                .recommendations li {{
                    margin-bottom: 10px;
                }}
                
                .closing {{
                    margin-top: 30px;
                    font-style: italic;
                }}
                
                .badge-container {{
                    text-align: center;
                    margin: 30px 0;
                }}
                
                .badge {{
                    max-width: 150px;
                    height: auto;
                }}
                
                .footer {{
                    background-color: #2c3e50;
                    color: #ecf0f1;
                    text-align: center;
                    padding: 20px;
                    font-size: 14px;
                }}
                
                .footer p {{
                    margin: 5px 0;
                }}
                
                .social-links {{
                    margin: 15px 0;
                }}
                
                .social-links a {{
                    color: #ecf0f1;
                    margin: 0 10px;
                    text-decoration: none;
                }}
                
                .disclaimer {{
                    font-size: 12px;
                    color: #bdc3c7;
                    margin-top: 15px;
                }}
                
                .universidad-logo {{
                    max-width: 200px;
                    height: auto;
                    margin: 10px 0;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Tu Feedback Personalizado</h1>
                </div>
                
                <div class="logo-container">
                    <img src="cid:logo_wololo" class="logo" alt="Wololo Icon">
                    <span class="brand-text">WOLOLO</span>
                </div>
                
                <div class="content">
                    <div class="greeting">
                        <p>Hola <strong>{name}</strong>,</p>
                        <p>Gracias por utilizar nuestro Modelo Predictivo de Empleabilidad. A continuación, encontrarás un análisis personalizado basado en tu perfil:</p>
                    </div>
                    
                    <div class="profile">
                        <h3>Tu Perfil:</h3>
                        <ul>
                            <li><strong>Años de experiencia:</strong> {profile_info.get('experience')}</li>
                            <li><strong>Habilidades blandas:</strong> {profile_info.get('skills')}</li>
                            <li><strong>Lenguajes de programación:</strong> {profile_info.get('languages')}</li>
                            <li><strong>Predicción:</strong> <span class="prediction-badge">{profile_info.get('prediction')}</span></li>
                        </ul>
                    </div>
                    
                    <div class="analysis">
                        <h3>Análisis y Recomendaciones:</h3>
                        <div class="feedback-content">
                            {feedback}
                        </div>
                    </div>
                    
                    <div class="closing">
                        <p>Esperamos que este feedback te sea útil en tu desarrollo profesional.</p>
                        <p>¡Mucho éxito en tu carrera!</p>
                    </div>
                </div>
                
                <div class="footer">
                    <img src="cid:logo_universidad" class="universidad-logo" alt="Universidad de Cundinamarca">
                    <p>© Universidad de Cundinamarca - Modelo Predictivo de Empleabilidad</p>
                    <div class="social-links">
                        <a href="">Visita nuestra página web</a>
                    </div>
                    <p class="disclaimer">Este es un correo automático. Por favor, no respondas a este mensaje.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Adjuntar parte HTML
        part = MIMEText(html, "html")
        msgAlternative.attach(part)
        
        # Obtener la ruta base del proyecto
        base_path = pathlib.Path(__file__).parent.parent.absolute()
        
        # Rutas de imágenes con rutas absolutas (actualizadas para usar las imágenes correctas)
        img_paths = {
            'logo_universidad': os.path.join(base_path, 'static', 'img', 'imagotipo', 'IMAGOTIPO HORIZONTAL NEGRO.png'),
            'logo_wololo': os.path.join(base_path, 'static', 'Wololo Icon.png')
        }
        
        # Verificar si las imágenes existen antes de intentar adjuntarlas
        for img_id, img_path in img_paths.items():
            if os.path.exists(img_path):
                with open(img_path, 'rb') as img:
                    img_data = MIMEImage(img.read())
                    img_data.add_header('Content-ID', f'<{img_id}>')
                    message.attach(img_data)
                print(f"Imagen {img_id} adjuntada correctamente desde {img_path}")
            else:
                print(f"ADVERTENCIA: No se encontró la imagen {img_id} en {img_path}")
                print(f"Directorio actual: {os.getcwd()}")
                print(f"Contenido del directorio de imágenes: {os.listdir(os.path.dirname(img_path)) if os.path.exists(os.path.dirname(img_path)) else 'Directorio no existe'}")
        
        # Iniciar conexión segura con el servidor
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        
        # Enviar correo
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
        
        print(f"Correo enviado exitosamente a {recipient_email}")
        return True
    
    except Exception as e:
        print(f"Error al enviar correo: {str(e)}")
        return False