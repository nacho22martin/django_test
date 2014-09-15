$(function() {
	$('.carousel3').carouFredSel({
		items: 1,
		responsive:true,
		scroll: {
			onAfter: function() {
				setRandomFX( $(this) );
			}
		},
		onCreate: function() {
			setRandomFX( $(this) );
		}
	});
});
var allFXs = [ 'scroll', 'crossfade', 'cover', 'uncover' ];
function setRandomFX( $elem ) {
	var newFX = Math.floor( Math.random() * allFXs.length );
	$elem.trigger( 'configuration', {
		auto: {
			fx: allFXs[ newFX ]
		}
	});
}