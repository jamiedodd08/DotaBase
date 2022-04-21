function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

function sortbystrength() {
  document.getElementById("sortimg").style.display='block';
  document.getElementById("sortimg").src = "static/images/strength.png";
  [].forEach.call(document.querySelectorAll('.strengthhero'), function (hidden) {
    hidden.style.display = 'block';
  });
  [].forEach.call(document.querySelectorAll('.agilityhero'), function (hidden) {
    hidden.style.display = 'none';
  });
  [].forEach.call(document.querySelectorAll('.intelligencehero'), function (hidden) {
    hidden.style.display = 'none';
  });
  }

  function sortbyagility() {
  document.getElementById("sortimg").style.display='block';
  document.getElementById("sortimg").src = "static/images/agility.png";
  [].forEach.call(document.querySelectorAll('.agilityhero'), function (hidden) {
    hidden.style.display = 'block';
  });
  [].forEach.call(document.querySelectorAll('.strengthhero'), function (hidden) {
    hidden.style.display = 'none';
  });
  [].forEach.call(document.querySelectorAll('.intelligencehero'), function (hidden) {
    hidden.style.display = 'none';
  });
  }

  function sortbyintelligence() {
  document.getElementById("sortimg").style.display='block';
  document.getElementById("sortimg").src = "static/images/intelligence.png";
  [].forEach.call(document.querySelectorAll('.intelligencehero'), function (hidden) {
    hidden.style.display = 'block';
  });
  [].forEach.call(document.querySelectorAll('.agilityhero'), function (hidden) {
    hidden.style.display = 'none';
  });
  [].forEach.call(document.querySelectorAll('.strengthhero'), function (hidden) {
    hidden.style.display = 'none';
  });
  }

  function sortbyall() {
    document.getElementById("sortimg").style.display='none';
    [].forEach.call(document.querySelectorAll('.intelligencehero'), function (hidden) {
      hidden.style.display = 'block';
    });
    [].forEach.call(document.querySelectorAll('.agilityhero'), function (hidden) {
      hidden.style.display = 'block';
    });
    [].forEach.call(document.querySelectorAll('.strengthhero'), function (hidden) {
      hidden.style.display = 'block';
    });
    }