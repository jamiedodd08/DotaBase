function hidecounters(x) {
    var g = document.querySelector('.herocounterto');
    var j = document.querySelector('.herocounteredby');
    x.classList.toggle("fa-eye-slash");
    if(g.style.display === "none") {
        g.style.display = "block";
        j.style.display = "block";
    }

    else {
        g.style.display = "none";
        j.style.display = "none";
    }
  }

function hideitems(x) {
    var g = document.querySelector('.itemsforcontainer');
    var j = document.querySelector('.itemsagainstcontainer');
    x.classList.toggle("fa-eye-slash");
    if(g.style.display === "none") {
        g.style.display = "block";
        j.style.display = "block";
    }

    else {
        g.style.display = "none";
        j.style.display = "none";
    }
  }

function hideabilities(x) {
    var g = document.querySelector('.heroabilities');
    x.classList.toggle("fa-eye-slash");
    if(g.style.display === "none") {
        g.style.display = "block";
    }
    else {
        g.style.display = "none";
    }
}



$('document').ready(function(){
    $('.infocontainer>.itemtxt>p:empty').closest('.infocontainer').hide();
    
    $('.addabilitybtn').click(function(){
        if ($('.userid').is(':empty')){
            $(location).prop('href', '/login');
        }
        else {
            $(this).parent().parent().find('.addabilityinfo').toggle(300);
            $(this).toggleClass('fa-circle-plus fa-circle-minus');
        }
    });

    $('.addinfo').click(function(){
        if ($('.userid').is(':empty')){
            $(location).prop('href', '/login');
            alert("Please login or create an account to access this feature!");
        }
        else {
            $(this).parent().find('.formcontainer').toggle(300);
            $(this).toggleClass('fa-circle-plus fa-circle-minus');
        }
    });

    $('.vote').click(function(){
        if ($('.userid').is(':empty')){
            alert("Please login or create an account to access this feature!");
        }
    });

    $('.titleanditemabilities>.itemabilitycontainter>.itemability1>.itemabilitytxt>p:empty').closest('.titleanditemabilities').hide();
    $('.itemability>.itemabilitytxt>p:empty').closest('.itemability').hide();

    $('.userupvote').each(function(){
        if ($(this).is(':empty')){
        }
        else {
            $(this).parent().find('.fa-thumbs-up').css("color", "greenyellow");
        }   
    });

    $('.userdownvote').each(function(){
       
        if ($(this).is(':empty')){
        }
        else {
            $(this).parent().find('.fa-thumbs-down').css("color", "red");
        }
    });

    $('.closeicon').click(function(){
        $('.flashmsg').hide();
    });

    $('.errorbtn').click(function(){
        $(location).prop('href', '/home');
    });

    $('.opendeleteform').click(function(){
        $(this).parent().find('.formpopup').css('display','block');
        $(this).css('display','none');
    });

    $('.cancel').click(function(){
        $(this).parent().parent().parent().find('.formpopup').css('display','none');
        $(this).parent().parent().parent().find('.opendeleteform').css('display','block');
    });

});
