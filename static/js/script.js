const nav = document.querySelector('.nav')

window.addEventListener('scroll', fixedNav)


function fixedNav() {
    if(window.scrollY > nav.offsetHeight +150) {
        nav.classList.add('active')
    } else {
        nav.classList.remove('active')
    }
}

function myFunction() {
    var x = document.querySelector(".nav");
    if (x.className === "nav") {
      x.className += " responsive";
    } else {
      x.className = "nav";
    }
  }