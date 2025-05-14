document.addEventListener('DOMContentLoaded', function() {
    // Referencias a elementos del DOM
    const contactForm = document.getElementById('contactForm');
    const confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
    
    // Manejar envío del formulario
    contactForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        // Aquí normalmente enviarías los datos a un servidor
        // Simulamos una petición con un timeout
        const submitButton = contactForm.querySelector('button[type="submit"]');
        const originalText = submitButton.innerHTML;
        
        // Cambiar el botón a estado de carga
        submitButton.disabled = true;
        submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Enviando...';
        
        // Simular envío (reemplazar con tu lógica de envío real)
        setTimeout(() => {
            // Restablecer el botón
            submitButton.disabled = false;
            submitButton.innerHTML = originalText;
            
            // Mostrar modal de confirmación
            confirmationModal.show();
            
            // Limpiar el formulario
            contactForm.reset();
        }, 1500);
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