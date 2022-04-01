function hidecounters(x) {
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

function hideitems(x) {
    var g = document.querySelector('.itemsforcontainer');
    var j = document.querySelector('.itemsagainstcontainer');
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

function hideabilities(x) {
    var g = document.querySelector('.heroabilities');
    x.classList.toggle("fa-eye-slash");
    if(g.style.display === "none") {
        g.style.display = "block";
    }
    else {
        g.style.display = "none";
    }
}
