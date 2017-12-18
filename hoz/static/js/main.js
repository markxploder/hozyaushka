function popOut(x) {
    x.classList.toggle("change");
    document.getElementById('header-menu').classList.toggle("change");
}
$(document).ready(function() {
	$(".carousel-inner").swipe( {
		swipeLeft:function(event, direction, distance, duration, fingerCount) {
			$(this).parent().carousel('next');
		},
		swipeRight: function() {
			$(this).parent().carousel('prev');
		},
		threshold:0
	});
});
