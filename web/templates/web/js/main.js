function classToggle() {
    document.querySelector('.header-nav').classList.toggle('active');
}

function positionFix() {
    document.querySelector('body').classList.toggle('fixed');
}

document.querySelector('.menu-toggle').addEventListener('click', classToggle);
document.querySelector('.menu-toggle').addEventListener('click', positionFix);

function flip() {
    this.querySelector('.gadget-front').classList.toggle('hidden');
    this.querySelector('.gadget-text').classList.toggle('show');
}

document.querySelector('.first').addEventListener('click', flip);
document.querySelector('.second').addEventListener('click', flip);
document.querySelector('.third').addEventListener('click', flip);
document.querySelector('.menu-toggle').addEventListener('click', classToggle);
document.querySelector('.menu-toggle').addEventListener('click', positionFix);
