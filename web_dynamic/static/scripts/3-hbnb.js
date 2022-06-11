document.addEventListener('DOMContentLoaded', () => {
    // check checkboxes that are cheked and storage in a list. 
    //Show the list in .amenities h4
    const checked_list = {};
    const checkbox = document.querySelectorAll('input[type=checkbox]').forEach(function (checks) {
        checks.addEventListener("change", function () {
            if (this.checked) {
                checked_list[checks.getAttribute('data-id')] = checks.getAttribute('data-name');
            }
            else {
                delete checked_list[checks.getAttribute('data-id')];
            }
            document.querySelector(".amenities h4").textContent = Object.values(checked_list).join(', ');
        });
    });
// status ip. IF status = 'OK' background is red with the available class
// else is grey
    const api_status = document.querySelector('div#api_status');
    fetch("http://localhost:5001/api/v1/places_search/").then((response) => {
        if (response.ok) {
            api_status.className += ".available";
        }
        else {
            api_status.className.replace(".available", '');
        }
    });
// 
    function fetchPlaces() {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", 'http://0.0.0.0:5001/api/v1/places_search', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({
            value: value
        }));
    }
});
