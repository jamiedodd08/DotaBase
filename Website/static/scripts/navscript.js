window.onload=function(){
    var toggleButton = document.querySelector('.togglebutton');
    var navbarLinks = document.querySelector('.nav-links');
    toggleButton.addEventListener('click', function(){
        navbarLinks.classList.toggle('active');
    });
}