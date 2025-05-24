document.addEventListener('DOMContentLoaded', function() {
    // Referencias a elementos del DOM
    const contactForm = document.getElementById('contactForm');
    const confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
    const emailInput = document.getElementById('emailInput');
    const mensajeTextarea = document.getElementById('mensajeTextarea');
    
    // Función para validar campos
    function validarCampo(campo) {
        if (!campo.value.trim()) {
            campo.classList.remove('is-valid');
            campo.classList.add('is-invalid');
            return false;
        } else {
            campo.classList.remove('is-invalid');
            campo.classList.add('is-valid');
            return true;
        }
    }
    
    // Validar en tiempo real cuando el usuario escribe
    emailInput.addEventListener('input', function() {
        validarCampo(this);
    });
    
    mensajeTextarea.addEventListener('input', function() {
        validarCampo(this);
    });
    
    // Manejar envío del formulario
    contactForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        // Obtener los datos del formulario
        const nombre = document.getElementById('nombreInput').value;
        const email = emailInput.value;
        const mensaje = mensajeTextarea.value;
        
        // Validar campos requeridos
        const emailValido = validarCampo(emailInput);
        const mensajeValido = validarCampo(mensajeTextarea);
        
        // Si algún campo requerido no es válido, detener el envío
        if (!emailValido || !mensajeValido) {
            return;
        }
        
        // Cambiar el botón a estado de carga
        const submitButton = contactForm.querySelector('button[type="submit"]');
        const originalText = submitButton.innerHTML;
        submitButton.disabled = true;
        submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Enviando...';
        
        // Crear FormData para enviar
        const formData = new FormData();
        formData.append('nombre', nombre);
        formData.append('email', email);
        formData.append('mensaje', mensaje);
        
        // Enviar solicitud AJAX
        fetch('/enviar_contacto', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Restablecer el botón
            submitButton.disabled = false;
            submitButton.innerHTML = originalText;
            
            if (data.success) {
                // Mostrar modal de confirmación
                confirmationModal.show();
                
                // Limpiar el formulario y las clases de validación
                contactForm.reset();
                emailInput.classList.remove('is-valid', 'is-invalid');
                mensajeTextarea.classList.remove('is-valid', 'is-invalid');
            } else {
                // Mostrar mensaje de error en el formulario
                const errorDiv = document.createElement('div');
                errorDiv.className = 'alert alert-danger mt-3';
                errorDiv.textContent = 'Error al enviar el mensaje: ' + data.message;
                contactForm.appendChild(errorDiv);
                
                // Eliminar el mensaje después de 5 segundos
                setTimeout(() => {
                    errorDiv.remove();
                }, 5000);
            }
        })
        .catch(error => {
            // Restablecer el botón
            submitButton.disabled = false;
            submitButton.innerHTML = originalText;
            
            console.error('Error:', error);
            
            // Mostrar mensaje de error en el formulario
            const errorDiv = document.createElement('div');
            errorDiv.className = 'alert alert-danger mt-3';
            errorDiv.textContent = 'Error al enviar el mensaje. Por favor, intenta nuevamente.';
            contactForm.appendChild(errorDiv);
            
            // Eliminar el mensaje después de 5 segundos
            setTimeout(() => {
                errorDiv.remove();
            }, 5000);
        });
    });
    
    // Efectos visuales para los campos del formulario
    const formInputs = document.querySelectorAll('.form-control');
    
    formInputs.forEach(input => {
        // Efecto de enfoque
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('input-focused');
        });
        
        // Efecto al perder el enfoque
        input.addEventListener('blur', function() {
            if (!this.value) {
                this.parentElement.classList.remove('input-focused');
            }
            // Validar al perder el foco si es un campo requerido
            if (this.hasAttribute('required')) {
                validarCampo(this);
            }
        });
    });
    
    // Animación para las tarjetas de desarrolladores
    const devCards = document.querySelectorAll('.dev-card');
    
    devCards.forEach((card, index) => {
        // Añadir un pequeño retraso para cada tarjeta
        card.style.animationDelay = `${index * 0.2}s`;
        
        // Efecto de hover para mostrar información adicional
        card.addEventListener('mouseenter', function() {
            this.classList.add('card-hovered');
        });
        
        card.addEventListener('mouseleave', function() {
            this.classList.remove('card-hovered');
        });
    });
});