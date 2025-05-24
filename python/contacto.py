import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv
import pathlib

load_dotenv()

def enviar_mensaje_contacto(email, nombre, mensaje):
    """
    Envía un correo electrónico con el mensaje de contacto del usuario.
    
    Args:
        email (str): Correo electrónico del remitente
        nombre (str): Nombre del remitente (opcional)
        mensaje (str): Mensaje enviado por el usuario
    
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
        message["Subject"] = "Nuevo mensaje de contacto - Modelo Predictivo"
        message["From"] = sender_email
        message["To"] = sender_email  # El correo se envía al mismo correo configurado en .env
        message["Reply-To"] = email  # Para poder responder directamente al remitente
        
        # Parte alternativa para clientes que no pueden ver HTML
        msgAlternative = MIMEMultipart('alternative')
        message.attach(msgAlternative)
        
        # Usar nombre o 'Usuario' si está vacío
        nombre_mostrar = nombre if nombre else 'Usuario'
        
        # Crear versión HTML del mensaje
        html = f"""
        <html>
        <head>
            <style>
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
                }}
                
                .header h1 {{
                    margin: 0;
                    font-size: 28px;
                    font-weight: 700;
                }}
                
                .content {{
                    padding: 30px;
                    background-color: #ffffff;
                }}
                
                .message-info {{
                    background-color: #f0f4f8;
                    padding: 20px;
                    margin-bottom: 25px;
                    border-radius: 8px;
                    border-left: 5px solid #4a6fdc;
                }}
                
                .message-content {{
                    white-space: pre-line;
                    line-height: 1.8;
                    padding: 15px;
                    background-color: #f9f9f9;
                    border-radius: 8px;
                }}
                
                .footer {{
                    background-color: #2c3e50;
                    color: #ecf0f1;
                    text-align: center;
                    padding: 20px;
                    font-size: 14px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Nuevo Mensaje de Contacto</h1>
                </div>
                
                <div class="content">
                    <div class="message-info">
                        <p><strong>Nombre:</strong> {nombre}</p>
                        <p><strong>Correo electrónico:</strong> {email}</p>
                    </div>
                    
                    <h3>Mensaje:</h3>
                    <div class="message-content">
                        {mensaje if mensaje else "(Sin mensaje)"}
                    </div>
                </div>
                
                <div class="footer">
                    <p>© Universidad de Cundinamarca - Modelo Predictivo de Empleabilidad</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Adjuntar parte HTML
        part = MIMEText(html, "html")
        msgAlternative.attach(part)
        
        # Iniciar conexión segura con el servidor
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        
        # Enviar correo
        server.sendmail(sender_email, sender_email, message.as_string())
        server.quit()
        
        print(f"Correo de contacto enviado exitosamente desde {email}")
        return True
    
    except Exception as e:
        print(f"Error al enviar correo de contacto: {str(e)}")
        return False