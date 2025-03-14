Description
QReate is a simple web application that allows users to generate QR codes from links or text. 
This project uses Flask for the backend for handling dynamic QR code display.

Features

Convert any URL or text into a QR code.

Dynamically display the QR code.

Simple and clean user interface.

Technologies Used

Backend: Flask (Python)

Frontend: HTML, CSS

QR Code Generation: qrcode Python library

Installation

Prerequisites

Ensure you have Python installed. 

Setup

Clone the repository:

git clone https://github.com/yourusername/qreate.git
cd qreate

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:

  pip install flask qrcode[pil] pillow

Running the Application

Start the Flask server:

  python app.py

Open your browser and go to:

  http://127.0.0.1:5000/

Project Structure

qreate/
│-- static/
│   ├── styles.css    # Stylesheet for the frontend
│-- templates/
│   ├── index.html    # Main HTML file
│-- app.py           # Flask backend
│-- README.md        # Project documentation

Usage

 1. Enter a URL or text into the input field.
 2. Click the "Generate QR Code" button.
 3. The QR code will be displayed dynamically on the page.
