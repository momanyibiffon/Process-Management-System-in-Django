// #######################jQuery code#############################//
$(document).ready(function(){

    $('.fixed-action-btn').floatingActionButton({
        toolbarEnabled: true
     });
    //sidenav controller for materialize css
    $('.sidenav').sidenav();
    // dropdown initialization
    $('.dropdown-trigger').dropdown();
    //index page slider controller
    $('.slider').slider();
    // Pause slider
    $('.slider').slider('pause');
    // Start slider
    $('.slider').slider('start');
    // Next slide
    $('.slider').slider('next');
    // Previous slide
    $('.slider').slider('prev');

    //Dashboard tabs initialization
    $('.tabs').tabs();

    //select initialization
    $('select').formSelect();

    // collapsible initialization
    $('.collapsible').collapsible({
      accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
    });

});
// #######################jQuery code#############################//

// #######################JavaScript code#############################//
// Add active class to the current button (highlight it)



// #######################JavaScript code#############################//