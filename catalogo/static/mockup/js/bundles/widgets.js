
if (window.jQuery) {
  define( "jquery", [], function () {
    "use strict";
    return window.jQuery;
  } );
}

define([
  'jquery',
  'mockup-registry',
//   Uncomment the line below to include all patterns from plone-mockup
//   'mockup-bundles-widgets',
//   <!~~ Add patterns below this line ~~!>
  'augustorubio-patterns-carousel',
  'mockup-patterns-modal'
], function($, registry) {
  "use strict";

  var augustorubioWidgets = {
    name: "augustorubio-widgets",
    transform: function($root) {
    // The code you add here will be executed before scanning the DOM

    }
  };

  registry.register(augustorubioWidgets);

  // initialize only if we are in top frame
  if (window.parent === window) {
    $(document).ready(function() {
      registry.scan($('body'));
      
      // We don't want to ignore links inside modals
      $('.pat-modal').on('shown.modal.patterns', function(e) {
            $('div.modal.active').off('click')
            .on('click', function(e) {
            e.stopPropagation();
          });
      });
    });
  }

  return augustorubioWidgets;
});
