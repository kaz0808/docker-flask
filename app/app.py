from flask import Flask,request,redirect,render_template,send_from_directory
import os
 
app = Flask(__name__)
 
@app.route("/")
def home_page():
    dir_path = 'imgfile'

    files = os.listdir(dir_path)

    return render_template('index.html', files=files)

@app.route('/slideshow')
def slideshow():

    dir_path = 'imgfile'

    files = os.listdir(dir_path)

    return render_template('slideshow.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    upload_dir = 'imgfile'

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file.save(os.path.join(upload_dir, file.filename))
    return redirect('/')