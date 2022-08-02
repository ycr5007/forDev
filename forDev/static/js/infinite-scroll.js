$(function () {
  var $win = $(window);
  $win.scroll(function () {
    let diff = $(document).height() - $win.height() - 50;
    if (Math.ceil($(document).scrollTop()) > diff) {
      console.log("loading");
    }
  });
});
