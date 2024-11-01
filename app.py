import os
import math
import random
import smtplib
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

digits = "0123456789"
OTP = ""
for i in range(6): 
    OTP += digits[math.floor(random.random()*10)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_otp', methods=['POST'])
def send_otp():
    global OTP
    try:
        # Regenerate OTP each time
        OTP = ""
        for i in range(6): 
            OTP += digits[math.floor(random.random()*10)]
        
        otp = OTP + " is your OTP"
        
        # Email sending logic
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("your_email@gmail.com", "your_app_password")
        
        emailid = request.form.get('email')
        s.sendmail('your_email@gmail.com', emailid, otp)
        
        return jsonify({"status": "success", "message": "OTP sent successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    global OTP
    user_otp = request.form.get('otp')
    
    if user_otp == OTP: 
        return jsonify({"status": "success", "message": "Verified"})
    else: 
        return jsonify({"status": "error", "message": "Please Check your OTP again"})

if __name__ == '__main__':
    app.run(debug=True)
