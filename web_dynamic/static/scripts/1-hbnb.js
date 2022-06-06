window.onload = () => {

	const amenitiesDict = {};
	const amenities = document.querySelectorAll('.list_check');
	const checkbox = document.getElementById('list');
    const amenityName = document.getElementsByName('data-name');
    const amenityId = documnet.getElementsByName('data-id');


	checkbox.addEventListener('change', (event) => {
	  if (event.currentTarget.checked) {
        amenitiesDict.set(amenityId, amenityName);
	  } else {
		amenitiesDict.remove(amenityId);
	  }
	})
}
