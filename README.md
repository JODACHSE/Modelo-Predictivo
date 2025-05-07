# Proyecto de Predicción de Inserción Laboral

## Descripción

Este proyecto desarrollado con Flask y Bootstrap 5.3.5, esta diseñado para la implementacion de un modelo de predicción para predecir (valga la redundancia) la inserción laboral de estudiantes de Ingeniería en Sistemas y Computación. La aplicación web permite a los usuarios interactuar con el modelo de predicción a través de una interfaz sencilla y moderna.

## Estructura del Proyecto
```md
    Modelo-Predictivo/
    ├── app.py
    ├── requirements.txt
    ├── templates/
    │ ├── base.html
    │ ├── home.html
    │ └── pages/
    │ └── ModeloPredictivo.html
    └── static/
    ├── css/
    │ └── bootstrap.min.css
    └── js/
    └── bootstrap.bundle.min.js
```

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- npm (gestor de paquetes de Node.js)

## Instalación

1. **Clonar el repositorio:**

```bash
   git clone https://github.com/JODACHSE/Modelo-Predictivo
   cd Modelo-Predictivo
```
2. Crear y activar un entorno virtual:

```bash
python -m venv venv
# En Windows:
venv\\Scripts\\activate
# En macOS/Linux:
source venv/bin/activate
```

3. Instalar las dependencias de Python:

```bash
pip install -r requirements.txt
```

4. Instalar las dependencias de Node.js:

```bash
npm install
```

## Uso
Ejecutar la aplicación Flask:

```bash
flask --app app run --debug
```

La aplicación estará disponible en http://127.0.0.1:5000/.

### Abrir la aplicación en tu navegador:

Accede a http://127.0.0.1:5000/ para interactuar con la aplicación.

### Estructura de Archivos
* app.py: Archivo principal que contiene la configuración y las rutas de la aplicación Flask.

* requirements.txt: Lista de dependencias de Python necesarias para el proyecto.

* templates/: Directorio que contiene las plantillas HTML de la aplicación.

* base.html: Plantilla base que incluye la estructura común de la página.

* home.html: Página de inicio de la aplicación.

* pages/ModeloPredictivo.html: Página que muestra los resultados de la predicción.

* static/: Directorio que contiene los archivos estáticos como CSS y JavaScript.

* css/bootstrap.min.css: Archivo CSS de Bootstrap.

* js/bootstrap.bundle.min.js: Archivo JavaScript de Bootstrap.

# Contribución
Si deseas contribuir a este proyecto, por favor sigue estos pasos:

Fork el repositorio.

1. Crea una nueva rama para tu característica:

```bash
git checkout -b mi-nueva-caracteristica
```

2. Realiza tus cambios y haz commit:

```bash
git commit -am 'Añadir nueva característica'
```
3. Push a la rama:

```bash
git push origin mi-nueva-caracteristica
```
4. Crea un Pull Request.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.
