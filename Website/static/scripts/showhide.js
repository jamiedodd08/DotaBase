function myFunction(x) {
    var g = document.querySelector('.herocounterto');
    var j = document.querySelector('.herocounteredby');
    x.classList.toggle("fa-eye-slash");
    if(g.style.display === "none") {
        g.style.display = "block";
        j.style.display = "block";
    }

    else {
        g.style.display = "none";
        j.style.display = "none";
    }
  }



