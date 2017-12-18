var $circles = $(".circle"),
    tl = new TimelineMax();

function getRandomNumber() {
  return Math.floor(Math.random() * 10000);
}


TweenMax.set($circles, { scale: 0 });

tl.insert(
  TweenMax.staggerTo(
    $circles.toArray(),
    1,
    {
      opacity: 1,
      scale: 1,
      ease: Power1.easeIn
    },
    0.2
  )
);

tl.insert(
  TweenMax.staggerTo(
    $circles.toArray(),
    0.5,
    {
      scale: 1.2,
      boxShadow: "0 25px 25px rgba(0, 0, 0, 0.4)",
      repeat: -1,
      yoyo: true,
      ease: Power1.easeOut
    },
    0.2
  ),
  "-=0.4"
);


jQuery(document).ready(function($) {
  $(window).load(function() {
    setTimeout(function() {
      $('#preloader').fadeOut('slow', function() {});
    }, 2000);
  });
});
