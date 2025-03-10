from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    if request.method == 'POST':
        # Get data from form
        data = request.form['data']

        # Create the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image of the QR code
        img = qr.make_image(fill='black', back_color='white')

        # Save image to a BytesIO object
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)

        # Return image as a response
        return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
