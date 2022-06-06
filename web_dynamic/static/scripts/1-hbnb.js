window.onload = () => {
 //let amenities = document.querySelectorAll(".list")
  let prueba = document.getElementById(".amen_list");
  let select = document.getElementById("list_check")
  let amenity = [];

  const checkbox = document.getElementById('list')

  checkbox.addEventListener('change', (event) => {
	if (event.currentTarget.checked) {
	  alert('checked');
	} else {
	  alert('not checked');
	}
  })
}