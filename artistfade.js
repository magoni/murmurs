$(document).ready(function(){
  $("img").hover(function(){
    $(this).animate({opacity: 0.4}, 200);
    },function(){
    $(this).animate({opacity: 1.0}, 200);
  });
});
