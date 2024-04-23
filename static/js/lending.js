document.getElementById('showLoginBtn').addEventListener('click', function () {
    document.getElementById('loginContainer').style.display = 'block';
    document.getElementById('registerContainer').style.display = 'none';
});

document.getElementById('showRegisterBtn').addEventListener('click', function () {
    document.getElementById('loginContainer').style.display = 'none';
    document.getElementById('registerContainer').style.display = 'block';
});

document.getElementById('registerForm').addEventListener('submit', function (event) {
    event.preventDefault();
    if (!this.checkValidity()) {
        displayErrorMessage('Please check your input and try again.');
        return;
    }
    showLoadingIndicator();
    const formData = new FormData(this);
    fetch('/registration/', {
        method: 'POST',
        credentials: 'same-origin',
        headers: {'X-CSRFToken': csrftoken},
        body: formData
    }).then(response => response.json()).then(data => {
        if (data.url) {
            window.location.href = data.url; // Redirect on success
        } else {
            hideLoadingIndicator();
            console.error('Registration failed:', data.answer);
            displayErrorMessage(data.answer);
        }
    }).catch(error => {
        hideLoadingIndicator();
        console.error('Error:', error);
        displayErrorMessage('Error: ' + error);
    });
});

document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault();
    if (!this.checkValidity()) {
        displayErrorMessage('Please check your input and try again.');
        return;
    }
    showLoadingIndicator();
    const formData = new FormData(this);
    fetch('/login/', {
        method: 'POST',
        credentials: 'same-origin',
        headers: {'X-CSRFToken': csrftoken},
        body: formData
    }).then(response => response.json()).then(data => {
        if (data.url) {
            window.location.href = data.url; // Redirect on success
        } else {
            hideLoadingIndicator();
            console.error('Login failed:', data.answer);
            displayErrorMessage(data.answer);
        }
    }).catch(error => {
        displayErrorMessage('Error: ' + error);
        hideLoadingIndicator();
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');