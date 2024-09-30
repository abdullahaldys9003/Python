from flask import Flask, request, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

# تأكد من وجود مجلد uploads
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return "No audio file part", 400

    file = request.files['audio']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))  # احفظ الملف في مجلد uploads
    return "File uploaded successfully", 200

if __name__ == '__main__':
    app.run(debug=True)
