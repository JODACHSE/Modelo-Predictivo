/****************************************************************
 *                          VARIABLES
 ****************************************************************/
const nav = document.getElementById('mainNavbar');
const logo = document.getElementById('logo');
const themeToggle = document.getElementById('themeToggle');
const htmlElement = document.documentElement;
const sunIcon = document.getElementById('sunIcon');
const moonIcon = document.getElementById('moonIcon');

/****************************************************************
 *                            RUTAS
 ****************************************************************/
const LOGO_DARK = logo.dataset.darkSrc;
const LOGO_LIGHT = logo.dataset.lightSrc;

/****************************************************************
 *                          FUNCIONES
 ****************************************************************/
function applyTheme() {
    const theme = htmlElement.getAttribute('data-bs-theme');
    const isDark = theme === 'dark';

    // Navbar
    if (isDark) {
        nav.classList.add('bg-dark', 'border-bottom', 'border-body');
        nav.style.backgroundColor = '';
    } else {
        nav.classList.remove('bg-dark', 'border-bottom', 'border-body');
        nav.style.backgroundColor = '#e3f2fd';
    }
    nav.setAttribute('data-bs-theme', theme);

    // Logo
    logo.src = isDark ? LOGO_DARK : LOGO_LIGHT;

    // Iconos
    sunIcon.style.display = isDark ? 'inline' : 'none';
    moonIcon.style.display = isDark ? 'none' : 'inline';
}

function initTheme() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        htmlElement.setAttribute('data-bs-theme', savedTheme);
    } else {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        htmlElement.setAttribute('data-bs-theme', prefersDark ? 'dark' : 'light');
    }
    applyTheme();
}

/****************************************************************
 *                          EVENTOS
 ****************************************************************/
themeToggle.addEventListener('click', () => {
    const nuevoTema = htmlElement.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark';
    htmlElement.setAttribute('data-bs-theme', nuevoTema);
    localStorage.setItem('theme', nuevoTema);
    applyTheme();
});

document.addEventListener('DOMContentLoaded', initTheme);
