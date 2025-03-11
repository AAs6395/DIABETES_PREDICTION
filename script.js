document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {
        const inputs = document.querySelectorAll("input");
        let isValid = true;

        inputs.forEach(input => {
            if (input.value.trim() === "") {
                isValid = false;
                alert(`Please fill out the ${input.name} field.`);
            }
        });

        if (!isValid) {
            event.preventDefault();
        }
    });
});
