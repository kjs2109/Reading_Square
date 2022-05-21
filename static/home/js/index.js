const toggleBtn = document.querySelector('.navbar-toggle');
const menu = document.querySelector('#menu');

toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
});