"""Server for POW, Shopify Backend Intern Challenge"""
from flask import (Flask, jsonify, render_template, request, flash, session, redirect)
import crud
import os
import cloudinary.uploader
import cloudinary.api
from datetime import datetime
from cloudinary.utils import cloudinary_url
from flask_cors import CORS, cross_origin
from model import connect_to_db, db, User, Image 
from hashlib import sha256

app = Flask(__name__)
CORS(app)
app.secret_key = "jenbrissman"
cloud_name = os.environ.get('cloud_name')
cloud_api_key = os.environ.get('cloud_api_key')
cloud_api_secret = os.environ.get('cloud_api_secret')
print(datetime.now())

###INSTANTIATING DB
connect_to_db(app)

#################################HOME###########################################

@app.route('/')
def show_home():
    """Shows homepage. Lets users with existing accounts login"""

    return render_template('home.html')

#########################CREATE_AN_ACCOUNT######################################
def hashed(password):
    return sha256(password.encode('utf-8')).hexdigest()

@app.route('/api/register', methods=["POST"])
def register_user():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    if crud.get_user_by_email(email) != None:
        return jsonify({'status': 'email_error', 'email': email})
    else:
        crud.create_user(first_name, last_name, email, hashed(password))
        return jsonify({'first_name': first_name, 'last_name': last_name})

######################################LOGIN###########################################

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user_obj = crud.get_user_by_email(email)
    if user_obj != None:
        if hashed(password) == user_obj.password:
            session['user_id'] = user_obj.user_id
            return redirect('/gallery')
        else:
            flash('Incorrect password, please try again')
    else:
        flash('You have not created an account with that email. Please create account')
    return redirect('/')

###############################UPLOAD ART##############################################

@app.route('/upload')
def display_upload_page():
    if 'user_id' in session:
        user_id = session['user_id']
        user = crud.get_user_by_id(session['user_id'])
        return render_template('upload.html', user=user)
    return redirect('/')

#######################SUBMIT IMAGE####################################################

@app.route('/submit-image', methods=["POST"])
def image():
    if 'user_id' not in session:
        return redirect('/')
    user_id = session['user_id']
    image_title = request.json.get('image_title')
    artist = request.json.get('artist')
    location = request.json.get('location')
    image_url = request.json.get('image_url')

    image_obj = crud.create_image(user_id, image_title, artist, location, image_url)
    
    return jsonify({'completed': True})

##################################UPLOAD CLOUDINARY##################################

@app.route("/upload-cloudinary", methods=['POST'])
@cross_origin()
def upload_file():
    #initializing cloudinary with the config
    cloudinary.config(cloud_name=cloud_name, api_key=cloud_api_key, api_secret=cloud_api_secret)
    upload_result = None
    file_to_upload = request.files['file']
    #if there is a file to upload, then upload to cloudinary
    if file_to_upload:
      upload_result = cloudinary.uploader.upload(file_to_upload, resource_type="auto")
      return jsonify(upload_result)

#########################CLOUDINARY OPTIMIZATION####################################################

@app.route("/cld_optimize", methods=['POST'])
@cross_origin()
def cld_optimize():
  app.logger.info('in optimize route')
  cloudinary.config(cloud_name = cloud_name, api_key=cloud_api_key, api_secret=cloud_api_secret)
  if request.method == 'POST':
    public_id = request.form['public_id']
    app.logger.info('%s public id', public_id)
    if public_id:
      cld_url = cloudinary_url(public_id, fetch_format='auto', quality='auto')
      app.logger.info(cld_url)
      return jsonify(cld_url)

#########################GALLERY####################################################

@app.route('/mygallery')
def my_gallery():
    """Lets users view and interact with their OWN gallery"""
    if 'user_id' not in session:
        return redirect("/")
    user = crud.get_user_by_id(session['user_id'])
    images = crud.get_image_by_user(user.user_id)
    
    return render_template('gallery.html', user=user, images=images)


@app.route('/gallery')
def gallery():
    """Lets users view and interact with gallery"""
    if 'user_id' not in session:
        return redirect("/")
    user = crud.get_user_by_id(session['user_id'])
    all_images = crud.get_all_images()
    print("hello!!!")
    print(all_images)
    
    return render_template('gallery.html', user=user, images=all_images)



#######################LOGOUT###############################################

@app.route('/logout')
def logout():
    print(session)
    if session['user_id']:
        session.pop('user_id')
        return redirect('/')
    else: 
        pass

#################################RUN###################################################
 

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', port=5001, debug=True)