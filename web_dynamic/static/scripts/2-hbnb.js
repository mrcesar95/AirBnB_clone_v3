document.addEventListener('DOMContentLoaded', () => {
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

    const api_status = document.querySelector('div#api_status');
    fetch("http://localhost:5001/api/v1/status/").then((response) => {
        if (response.ok) {
            api_status.className += " available";
        }
        else {
            api_status.className.replace(" available", '');
        }
    });
});

