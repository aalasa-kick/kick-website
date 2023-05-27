const customNav = document.querySelector('.custom-nav');

window.addEventListener('scroll', () => {
    if(window.scrollY > 450) {
        customNav.classList.add('custom-nav-scrolled');
    } else if (window.scrollY <= 450) {
        customNav.classList.remove('custom-nav-scrolled');
    }
})

function myFunction() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }
  
  $(document).ready(function(){
      $('#nav-icon4').click(function(){
          $(this).toggleClass('open');
      });
  });