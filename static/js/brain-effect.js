window.onload = function () {
  var Line1 = document.getElementById("line1");
  var Line2 = document.getElementById("line2");
  //Add paths together
  Line1.setAttribute('d', Line1.getAttribute('d') + '' + Line2.getAttribute('d'));
  //Remove unnecessary second path
  Line2.parentNode.removeChild(Line2);
}