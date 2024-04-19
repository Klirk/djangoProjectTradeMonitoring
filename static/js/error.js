function displayErrorMessage(message) {
        let errorContainer = document.createElement('div');
        errorContainer.classList.add('error-message');
        errorContainer.textContent = message;

        document.body.appendChild(errorContainer);

        setTimeout(function () {
            errorContainer.remove();
        }, 5000);
    }