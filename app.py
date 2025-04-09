from flask import Flask, render_template, request, redirect, url_for
import os
from PIL import Image

app = Flask(__name__)

# Папка для загрузки изображений
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Обрезаем изображение до квадрата
        img = Image.open(file_path)
        img = img.resize((250, 250), Image.LANCZOS)
        img.save(file_path)
        
        return render_template('index.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)