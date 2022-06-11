document.addEventListener('DOMContentLoaded', () =>{
    const checklist = {};
    const checkbox = document.querySelectorAll('input[type=checkbox]');
    checkbox.forEach(check => check.addEventListener('change', function(){
        if(this.checked){
            checklist[check.getAttribute('data-id')] = check.getAttribute('data-name');
        } else {
            delete checklist[check.getAttribute('data-id')];
        }
        document.querySelector(".amenities h4").textContent = Object.values(checklist).join(', ');
    }))

})