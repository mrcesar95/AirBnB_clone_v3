window.onload = () => {
  const checked = [];
  const checkbox = $('.amenities input[type="checkbox"]');

  checkbox.addEventListener('click', function() {
    if(checkbox.checked){
      checked = ('.amenity.id')
    } else {
      const element = document.getElementById("amenity.id");
      element.remove('.amenity.id');
    }
  })

};