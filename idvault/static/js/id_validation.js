$(document).ready(function () {
    const $idInput = $('input[name="id_number"]');
    const $searchButton = $('#searchButton');

    // Function to validate SA ID Number (checks for exactly 13 digits)
    function validateIdNumber(value) {
        const regex = /^\d{13}$/; // Regex for exactly 13 digits
        return regex.test(value);
    }

    // Add input event listener for validation using jQuery
    $idInput.on('input', function () {
        if (validateIdNumber($idInput.val())) {
            $searchButton.prop('disabled', false);
            $idInput.removeClass('is-invalid').addClass('is-valid');
        } else {
            $searchButton.prop('disabled', true);
            $idInput.removeClass('is-valid').addClass('is-invalid');
        }
    });
});