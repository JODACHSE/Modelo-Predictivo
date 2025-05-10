document.addEventListener('DOMContentLoaded', () => {
    const dropdown = document.querySelector('.on-this-page');
    if (!dropdown) return;

    let timeoutId;
    let isVisible = true;

    const hideDropdown = () => {
        if (isVisible) {
            dropdown.style.opacity = '0';
            dropdown.style.pointerEvents = 'none';
            isVisible = false;
        }
    };
    
    const showDropdown = () => {
        if (!isVisible) {
            dropdown.style.opacity = '1';
            dropdown.style.pointerEvents = 'auto';
            isVisible = true;
        }

        clearTimeout(timeoutId);
        timeoutId = setTimeout(hideDropdown, 3000);
    };
    
    timeoutId = setTimeout(hideDropdown, 3000);

    window.addEventListener('scroll', showDropdown);
    document.addEventListener('mousemove', showDropdown);
});

window.addEventListener('load', () => {
    document
    .querySelectorAll('#evaluacion-datos .flip-card')
    .forEach(card => {
        const front = card.querySelector('.flip-card-front');
        const back  = card.querySelector('.flip-card-back');
        const h = Math.max(front.scrollHeight, back.scrollHeight);
        card.style.minHeight = h + 'px';
        card.querySelector('.flip-card-inner').style.minHeight = h + 'px';
    });
});
