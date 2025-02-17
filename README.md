# Etn-Swiftpay
Seamless ETN Crypto Payments via QR Code

Project Overview 
  ETN SwiftPay is a simple and secure crypto payment gateway that allows users to generate a QR code for Electroneum (ETN) payments. Built using Flask for the backend and       HTML/CSS/JavaScript for the frontend, it enables smooth and fast transactions.  

Features 
  Generate QR codes for ETN payments  
  Simple and user-friendly interface  
  Secure backend processing with Flask  
  Supports real-time transaction validation  
  Works on desktop and mobile browsers  

Tech Stack 
  Frontend: HTML, CSS, JavaScript  
  Backend: Flask (Python)  
  API: Flask-based transaction processing  
  Hosting: Can be hosted locally or on platforms like Heroku  

Installation & Setup  

Prerequisites 
  Ensure you have the following installed:  
  Python 3.x  
  Pip (Python package manager)  

Step 1: Clone the Repository 
  git clone https://github.com/yourusername/etn-swiftpay.git
  cd etn-swiftpay

Step 2: Install Dependencies 
  pip install flask flask-cors

Step 3: Run the Backend Server 
  python server.py

The Flask server will start at `http://127.0.0.1:5000`  

Step 4: Open the Frontend 
  1. Open `etn.html` in a web browser.  
  2. Enter an amount and click Generate QR Code.  
  3. Scan the QR code to proceed with the payment.  

Project Demo  
  Host this project using Heroku, Render, or any cloud service.  

Troubleshooting  
If you get a `ModuleNotFoundError`, run:  
  pip install flask flask-cors
If the server doesn’t start, check if port 5000 is already in use. Change the port in `server.py`:  
  app.run(debug=True, port=5001)

Future Improvements  
  Add real-time transaction validation  
  Enable multi-crypto support  
  Improve UI/UX for better user experience  
