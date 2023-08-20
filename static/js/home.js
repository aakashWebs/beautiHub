$(document).ready(function() {
  // Image index for navigation
  var currentImageIndex;

  // Show the modal and set the clicked image
  $(".image-popup").click(function() {
    var imgSrc = $(this).attr("src");
    currentImageIndex = $(".image-popup").index(this);
    console.log(currentImageIndex);
    showImage(imgSrc);
  });

  // Show the previous image when previous icon is clicked
  $(".prev").click(function() {
    currentImageIndex = (currentImageIndex - 1 + $(".image-popup").length) % $(".image-popup").length;
    var imgSrc = $(".image-popup").eq(currentImageIndex).attr("src");
    showImage(imgSrc);
  });

  // Show the next image when next icon is clicked
  $(".next").click(function() {
    currentImageIndex = (currentImageIndex + 1) % $(".image-popup").length;
    var imgSrc = $(".image-popup").eq(currentImageIndex).attr("src");
    showImage(imgSrc);
  });

  // When the close button in the modal is clicked, hide the modal
  $(".close").click(function() {
    $("#myModal").css("display", "none");
  });

  // Function to show the modal and set the image source
  function showImage(imgSrc) {
    $("#myModal").css("display", "block");
    $("#imgModal").attr("src", imgSrc);
  }
});