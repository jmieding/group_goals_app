$(document).ready(function() {

  $('i.fa-chevron-down').click(function() {
    $(this).toggleClass('rotate');
    var userGoals = $(this).closest('tr').nextUntil('.user');
    $(userGoals).toggleClass('nested-goal');
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