// =======================toggle icon navbar================*/
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');

};

// =======================scroll section avtiv link================*/

let sections = document.querySelectorAll('section')
let navlinks = document.querySelectorAll('header nav a')


window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset + height) {
            navlinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*='+ id +']').classList.add('active');
            });
        };
        
      });
      // ==============stiky nabar=================\\
      let header = document.querySelector('header');
      
      header.classList.toggle('sticky', window.scrollY > 100);
      
      // ==============remove toggle and navbar when click navbar link (scroll)=================\\
      menuIcon.classList.remove('bx-x');
      navbar.classList.remove('active');
      
      
    };


      // ================scroll reveal===============\\
      ScrollReveal({
        reset: true,
        distance:'80px',
        duration:2000,
        delay:200,
    });

    ScrollReveal().reveal('.home-content, .heading', { origin:'top' });
    ScrollReveal().reveal('.home-img, .services-container, .portfolio-box, .contact form', { origin:'bottom' });

    ScrollReveal().reveal('.home-content h1 , .about-img', { origin:'left' });
    ScrollReveal().reveal('.home-content p , .about-content', { origin:'right' });


      // ================typed-js===============\\


      const typed = new Typed('.multiple-text', {
          strings:['M.B.B.S','M.D',
          'D.N.B',' F.C.P.F', 'Medicine',
          'M.B.B.S', 'D.G.O ','M.S Genrelsurgeon',
          'M.B.B.S' ,'D.M.R.E ', 'M.D  ','D.M.R.D Radiologest', 
          'E.N.T',
          'B.A.M.S', ' M.D Pediatrici',
          'D.N.B ',' M.D ', ' Dermatolo',
          'D.M Cardiolo',
          'M.S.D.N.B Ortho',
          'Genrel Surge',
          'Neuro Physicion', 'Neuro Surgeon',
                      'Neprologist' ],
          typSpeed:100,
          backSpeed:100,
          backDelay:1000,
          loop:true  
      });