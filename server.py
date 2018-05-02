import os
from flask import Flask, render_template, request

UPLOAD_FOLDER = 'tmp'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/train')
def train_function():
   return render_template('train.html')

@app.route('/classify')
def classify_function():
    return render_template('classify.html')

@app.route('/upload-file', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return 'Upload Successfully'

@app.route('/classify-upload', methods = ['GET', 'POST'])
def classify_upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join('classify-tmp', f.filename))
        return 'Upload to classify successful, just todo something ...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug = True)