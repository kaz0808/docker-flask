from flask import Flask
from flask import render_template
from flask import request
 
app = Flask(__name__)
 
@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/chenge1")
def chenge1_page():
    return render_template('chenge1.html')

@app.route("/chenge2",methods=['POST'])
def chenge2_page():
    if request.method == 'POST':
     content = request.form.get('content')
     return render_template('chenge2.html',content=content)