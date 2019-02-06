$(document).ready(function(){
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('.fixed-action-btn').floatingActionButton();
    $('#scroll').click(function(){
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });
});
