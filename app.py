import os
from flask import Flask, send_file, request, jsonify
from werkzeug.exceptions import BadRequest
from werkzeug.utils import secure_filename


from Object_detection_image import detects
import time
import pyrebase

print("outside attendance")

# Example
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
app = Flask(__name__)


@app.route('/', methods=["POST"])
def attendance():
	# enter your firebase conection details here
    config = {
    "apiKey": 
    "authDomain": 
    "databaseURL": 
    "storageBucket": 
    }

    firebase = pyrebase.initialize_app(config)

    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password("user email ", "password")
    user['idToken']
    db = firebase.database()
    input_file = request.files.get('file')
    if not input_file:
        return BadRequest("File not present in request")

    filename = secure_filename(input_file.filename)
    if filename == '':
        return BadRequest("File name is not present in request")
    if not allowed_file(filename):
        return BadRequest("Invalid file type")

    input_filepath = os.path.join('./', filename)
    input_file.save(input_filepath)
    detected_p=detects(filename)
    
    lastdetected = { "last_detected" : str(detected_p) }
    db.child("UserID").update(lastdetected, user['idToken'])
    
    key=time.time()
    temp=int(round((key-int(key))*1000000,0))
    temp1=int(key)
    kp=str(temp1)+"_"+str(temp)
    
    lastdetected = { kp : str(detected_p) }
    print(lastdetected)
    db.child("UserID").child("history").update(lastdetected, user['idToken'])
    
    return jsonify(answer=str(detected_p))


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run(host='0.0.0.0')