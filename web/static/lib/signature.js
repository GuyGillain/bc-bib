setInterval(function() {
  var links = document.getElementsByTagName('a');
  var found = false;
  for (var i = 0; i < links.length; i++) {
    if (links[i].textContent === "Book") {
      found = true;
      break;
    }
  }
  if (found) {
    if (!document.getElementById('signature')) {
      var customText = document.createElement('div');
      customText.id = 'signature';
      customText.innerHTML = "<div style='position:fixed; bottom:10px; text-align:center; width:100%; font-size:110%; font-weight:bold;'><i class='fa fa-terminal' aria-hidden='true' style='color:purple'></i> Delire - Gillain - Varlet <i class='fa fa-thumbs-up' aria-hidden='true' style='color:green'></i> </div>"
      document.body.appendChild(customText);
    }
  } else {
    var customText = document.getElementById('signature');
    if (customText) {
      customText.parentNode.removeChild(customText);
    }
  }
}, 1000);