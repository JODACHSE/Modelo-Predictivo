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