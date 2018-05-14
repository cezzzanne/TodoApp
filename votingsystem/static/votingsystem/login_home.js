$(document).ready(function () {
    'use strict';
    //$('.folder-adder').hide();
    $('#all-folders').fadeIn("slow");
    //Adding Todo Functionality
    $('.add-folder').click(function () {
        $('.folder-adder').show();
        return false;
    });

    $('.added-folder').click(function () {
        $('.folder-adder').hide();
        return false;
    });
});
