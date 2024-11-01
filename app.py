import os
import math
import random
import smtplib 
digits="0123456789"
OTP=""
for i in range(6): 
      OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("your_email@gmail.com", "your_app_password")  # Replace with your actual Gmail and App Password
emailid = input("Enter your email: ")
s.sendmail('your_email@gmail.com', emailid, msg)  # Replace with your actual Gmail
a = input("Enter Your OTP >>: ")
if a == OTP: 
    print("Verified")
else: 
    print("Please Check your OTP again")
