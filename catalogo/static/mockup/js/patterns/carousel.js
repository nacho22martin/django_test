
define([
  'jquery',
  'mockup-patterns-base',
  'jquery.carouFredSel'
], function($, Base) {
  "use strict";

  var carouselPattern = Base.extend({
    // The name for this pattern
    name: "carousel",

    defaults: {
      // Default values for attributes
    },

    init: function() {
      
        var self = this;
        self.$el.hover(
            function() {
            $('#carousel', self.$el).trigger( 'pause' );
            $('#carousel-thumbnails', self.$el).parent().animate({
                top: 280
            });
            }, function() {

            $('#carousel', self.$el).trigger( 'play' );
            $('#carousel-thumbnails', self.$el).parent().animate({
                top: 375
            });
            }
        );

        $('#carousel', self.$el).carouFredSel({
            scroll: {
            fx: 'crossfade',
            onBefore: function( data ) {
                $('#carousel-thumbnails', self.$el).trigger(
                    'slideTo',
                    [ $('#carousel-thumbnails img[alt='+ data.items.visible.attr( 'alt' ) +']',
                        self.$el), 
                        -2 ] );
            }
            }
        });

        $('#carousel-thumbnails', self.$el).carouFredSel({
            auto: false,
            items: {
            start: -2
            }
        });

        $('#carousel-thumbnails img', self.$el).click(function() {
            $('#carousel', self.$el).trigger( 'slideTo', [ $('#carousel img[alt='+ $(this).attr( 'alt' ) +']', self.$el) ] );

        }).css( 'cursor', 'pointer' );
    }
  });

  return carouselPattern;

});
