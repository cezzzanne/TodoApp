$(document).ready(function () {
    'use strict';
    $('.folder-adder').hide()
    //Adding Todo Functionality
    $('.addfolder').click(function () {
      'use strict';
       $('.folder-adder').show();
        return false;
    });

    $('.addedfolder').click(function () {
      'use strict';
      $('.folder-adder').hide();
       return false;
    });
});
