$(document).ready(function(){
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('.fixed-action-btn').floatingActionButton();
    $('.datepicker').datepicker();
    $('#scroll').click(function(){
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });
      $(".dropdown-trigger").dropdown({
   coverTrigger: false
});
});
