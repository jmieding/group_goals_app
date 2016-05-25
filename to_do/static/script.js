$(document).ready() 
  $("td a div").click(function() {
    if ($(this).children().length < 1) {
      $(this).append("<span class='fa fa-check-circle fa-lg'></span>");
      $(this).addClass("selected");
    } else {
      $(this).children().remove();
      $(this).removeClass("selected");
    }
  });
  // $.post( "/", { name: "John", time: "2pm" } );