/*jslint browser: true*/
/*global $, jQuery, alert*/
$(document).ready(function () {
    'use strict';
    $('.first_home').hide();
    $('.login-show-left').hide();
    $('.login-show-right').hide();
    $('.signup-show-left').hide();
    $('.signup-show-right').hide();


    $('.title').hover(function () {
        $('.first-home').fadeOut('slow');
    });

    $('.login-button').mouseenter(function () {
        $('.left-title').fadeOut('quick');
        $('.right-title').fadeOut('quick');

        $('.login-show-left').fadeIn('slow');
        $('.login-show-right').fadeIn('slow');

    }).mouseleave(function () {

        $('.left-title').fadeIn('slow');
        $('.right-title').fadeIn('slow');

        $('.login-show-left').fadeOut('quick');
        $('.login-show-right').fadeOut('quick');
    });


    $('.signup-button').mouseenter(function () {
        $('.left-title').fadeOut('quick');
        $('.right-title').fadeOut('quick');

        $('.signup-show-left').fadeIn('slow');
        $('.signup-show-right').fadeIn('slow');

    }).mouseleave(function () {
        $('.left-title').fadeIn('slow');
        $('.right-title').fadeIn('slow');
        $('.signup-show-left').fadeOut('quick');
        $('.signup-show-right').fadeOut('quick');
    });
});
