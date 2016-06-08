$(document).ready(function() {

  $('i.fa-chevron-down').click(function() {
    $(this).toggleClass('rotate');
    var nextGoal = $(this).closest('tr').next();
    while (true) {
      if ($(nextGoal).hasClass('user')) {
        break;
      } else {
        $(nextGoal).toggleClass('nested-goal');
        $(nextGoal) = nextGoal.next();
      }
    }
  });
  
  $('td a div').click(function() {
    if ($(this).children().length < 1) {
      $(this).append('<span class="fa fa-check-circle fa-lg"></span>');
      $(this).addClass('selected');
    } else {
      $(this).children().remove();
      $(this).removeClass('selected');
    }
  });
  
});