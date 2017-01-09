
  $(document).ready(function() {
	$("#twitter").click(function(){location.href="http://twitter.com/mitsubishiperu";});
    var offset = $("#menu_flotante").offset();
    var topPadding = 50;
    $(window).scroll(function() {
      if ($("#menu_flotante").height() < $(window).height() && $(window).scrollTop() > offset.top) {
        $("#menu_flotante").stop().animate({
          marginTop: $(window).scrollTop() - offset.top + topPadding
        });
      } else {
        $("#menu_flotante").stop().animate({
          marginTop: 10
        });
      };
    });
  });
   
  $(document).ready(function(){
	
    if (window.screen.width == 1024){
         
      $('#menu_flotante').removeClass('menu_normal');
      $('#menu_flotante').addClass('menu_floatderecha');
      $('#menu_flotante').mouseenter(mostrarMenu);
    }

    function ocultarMenu(){
      //console.log("oculto");
      $('#menu_flotante').off('mouseleave');
      $('#menu_flotante').animate({ 
          marginRight: '-=25'
        }, 200, function() {     
          $('#menu_flotante').css('overflow', 'hidden');
          $('#menu_flotante').mouseenter(mostrarMenu);
      });
    }

    function mostrarMenu(){  
      //console.log("visible");
      $('#menu_flotante').off('mouseenter'); 
      $('#menu_flotante').css('overflow', 'visible');
      $('#menu_flotante').animate({ 
          marginRight: '+=25'
        }, 270, function() {
          // Animation complete.
          $('#menu_flotante').mouseleave(ocultarMenu);
      });
    }

  });
