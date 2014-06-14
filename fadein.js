$(document).ready(function(){
    $('#container').animate({opacity : 1}, 500);
    $('.container').animate({opacity : 1}, 500);
    $('#head').animate({opacity : 1}, 1000);
    $('#nav a').mouseover(function(){
        $(this).animate({"opacity": 0.7}, 100);
    }).mouseout(function(){
        $(this).animate({"opacity": 1.0}, 100);
    });
});
