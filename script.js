function sendOTP() {
    const email = document.getElementById('email').value;
    const messageDiv = document.getElementById('message');

    if (!email) {
        messageDiv.innerHTML = 'Please enter an email';
        messageDiv.className = 'error';
        return;
    }

    fetch('/send_otp', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `email=${encodeURIComponent(email)}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            messageDiv.innerHTML = 'OTP sent successfully!';
            messageDiv.className = 'success';
            
            // Hide email section and show OTP section
            document.getElementById('email-section').style.display = 'none';
            document.getElementById('otp-section').style.display = 'block';
        } else {
            messageDiv.innerHTML = data.message;
            messageDiv.className = 'error';
        }
    })
    .catch(error => {
        messageDiv.innerHTML = 'An error occurred';
        messageDiv.className = 'error';
        console.error('Error:', error);
    });
}

function verifyOTP() {
    const otp = document.getElementById('otp').value;
    const messageDiv = document.getElementById('message');

    if (!otp || otp.length !== 6) {
        messageDiv.innerHTML = 'Please enter a valid 6-digit OTP';
        messageDiv.className = 'error';
        return;
    }

    fetch('/verify_otp', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `otp=${encodeURIComponent(otp)}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            messageDiv.innerHTML = 'OTP Verified Successfully!';
            messageDiv.className = 'success';
        } else {
            messageDiv.innerHTML = 'Invalid OTP. Please try again.';
            messageDiv.className = 'error';
        }
    })
    .catch(error => {
        messageDiv.innerHTML = 'An error occurred';
        messageDiv.className = 'error';
        console.error('Error:', error);
    });
}
