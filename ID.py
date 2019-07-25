import os,json
from shutil import copyfile
from flask import Flask, render_template, request,flash
from werkzeug import secure_filename
from passporteye import read_mrz
import shutil


app = Flask(__name__)
#app.secret_key = os.urandom(24)

#@app.route('/')
#def helloIndex():
#    return render_template('upload.html')

#@app.route('/passport',method=['POST'])
#def MRZ():
#    mrz = read_mrz("dummy.jpg")
#    mrz_data = mrz.to_dict()
#    return(mrz_data['country'])

#@app.route('/upload')
#def upload_file():
#   return render_template('upload.html')

@app.route('/')
@app.route('/index',methods=['GET'])
def entry():
   return render_template('index.html')


	
@app.route('/uploader', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
       if 'file' not in request.files:
           return "No file"
       else:
           f = request.files['file']
           filename = secure_filename(f.filename)           
           #Save to passporteye folder to process
           os.chdir("C:/Users/shahi/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/passporteye")
           file_path="C:/Users/shahi/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/passporteye/"+filename
           static_path="C:/Users/shahi/AppData/Local/Programs/Python/Python36-32/static/images/"+filename
           f.save(filename)
           mrz = read_mrz(filename)
           mrz_data = mrz.to_dict()

           #Save to static folder to view
           copyfile(filename, static_path)
           
           os.remove(filename)
           #return json.dumps(mrz_data)
           return render_template('results.html',the_name=mrz_data['names'],the_DOB=mrz_data['date_of_birth'],the_PassportNumber=mrz_data['number'],the_filename=filename)
                      
           #f = request.files['file']
           #filename = secure_filename(f.filename)
           #f.save(filename)
           #mrz = read_mrz(filename)
           #mrz_data = mrz.to_dict()
           #os.remove(filename)
           #return json.dumps(mrz_data)
               
           #return(mrz_data['country'])
           #f.save(secure_filename(f.filename))
           
           #mrz = read_mrz(f)
           #mrz_data = mrz.to_dict()
           #return(mrz_data['country'])
           #return 'file uploaded successfully'

@app.route('/uploaderRestForm', methods = ['POST'])
def upload_file_rest_form():
   if request.method == 'POST':
       if 'file' not in request.files:
          return "No file"
       else:
          f = request.files['file']
          filename = secure_filename(f.filename)
          #Save to passporteye folder to process
          os.chdir("C:/Users/shahi/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/passporteye")
          f.save(filename)
          mrz = read_mrz(filename)
          mrz_data = mrz.to_dict()
          os.remove(filename)
          return json.dumps(mrz_data)

@app.route('/uploaderRest', methods = ['POST'])
def upload_file_rest():
   if request.method == 'POST':
       if 'file' not in request.files:
           return "No file"
       else:
           f = request.files['file']
           filename = secure_filename(f.filename)           
           #Save to passporteye folder to process
           os.chdir("C:/Users/shahi/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/passporteye")
           f.save(filename)
           mrz = read_mrz(filename)
           mrz_data = mrz.to_dict()
           os.remove(filename)
           return json.dumps(mrz_data)


if __name__ =='__main__':
    app.run(debug=True)
