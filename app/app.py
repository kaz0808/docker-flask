from flask import Flask,request,redirect,render_template,send_from_directory
import os
 
app = Flask(__name__,static_folder='./imgfile')
 
@app.route("/")
def home_page():
    dir_path = 'imgfile'

    files = os.listdir(dir_path)

    return render_template('index.html', files=files)

@app.route('/slideshow',methods=['POST'])
def slideshow():

    dir_path = 'imgfile'

    files = os.listdir(dir_path)

    time = request.form.get('time')

    return render_template('slideshow.html', files=files,time=time)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    upload_dir = 'imgfile'

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file.save(os.path.join(upload_dir, file.filename))
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    file_name = request.form.get('filename')

    dir_path = 'imgfile/'

    os.remove(dir_path+file_name)
    return redirect('/')
    