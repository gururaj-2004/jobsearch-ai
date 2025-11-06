$(document).ready(function () {
  $("nav a").click(function () {
    $("nav a").removeClass("active");
    $(this).addClass("active");
  });

  $(".profile-pic").hover(
    function () {
      $(this).css("transform", "scale(1.1)");
    },
    function () {
      $(this).css("transform", "scale(1)");
    }
  );
});
