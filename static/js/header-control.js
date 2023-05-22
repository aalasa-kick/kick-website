const customNav = document.querySelector('.custom-nav');

window.addEventListener('scroll', () => {
    if(window.scrollY > 450) {
        customNav.classList.add('custom-nav-scrolled');
    } else if (window.scrollY <= 450) {
        customNav.classList.remove('custom-nav-scrolled');
    }
})