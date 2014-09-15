

$(function() {
         $('#images').carouFredSel({
          items: 1,
          direction: 'up',
          responsive: true,

          auto: {            
            /*play: false,*/
            duration: 850,        
            timeoutDuration: 3000,
            easing: 'quadratic',
            pauseOnHover: true,
            onBefore: function() {
              var index = $(this).triggerHandler( 'currentPosition' );
              if ( index == 0 ) {
                index = $(this).children().length;
              }
              $('#texts').trigger('slideTo', [ index, {
                fx: 'directscroll'
              }, 'prev' ]);
              
            }
          }

         });
         $('#texts').carouFredSel({
          items: 1,
          direction: 'up',
          responsive: true,
          auto: {                  
            play: false,            
            duration: 750,
            easing: 'quadratic'
          }
         });



      });
/*
window.addEvent("domready", function(e){
$("#1").on("click", function(){
  var SM = new SimpleModal({"width":600});
      SM.addButton("Action button", "btn primary", function(){
          this.hide();
      });
      SM.addButton("Cancel", "btn");
      SM.show({
        "model":"modal-ajax",
        "title":"Titulo",
        "param":{
          "url":"{% url vehiculo/about %}",
          "onRequestComplete": function(){ /* Action on request complete  }
        }
      });
  });
});*/

