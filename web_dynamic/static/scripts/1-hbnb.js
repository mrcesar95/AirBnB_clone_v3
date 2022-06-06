window.onload = () => {

	const amenitiesDict = {};
	const amenities = document.querySelectorAll('.list_check');
	
	const checkbox = document.getElementById('list');


	checkbox.addEventListener('change', (event) => {
	  if (event.currentTarget.checked) {
		alert('checked')
		;
	  } else {
		alert('not checked');
	  }
	})
}
