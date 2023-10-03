import os
print('current directory')
print(os.getcwd())

from flask import Flask, request, jsonify
#from flask_cli import FlaskCLI
from gevent.pywsgi import WSGIServer
from app.torch_utils import transform_image, get_prediction


# Create an app
app = Flask(__name__)

# Setting up debug mode        
if __name__ == '__main__':
    app.run(debug=True)
    #Production
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

# Define allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    # xxx.png
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/predict", methods=["POST"])
def predict():

    # error checking
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error': 'no file not supported'})
        
        try:
            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            prediction = get_prediction(tensor)
            data={'prediction': prediction.item(), 'class_name': str(prediction.item())}
            return jsonify(data)
        
        except:
            return jsonify({'error': 'error during prediction'})



        
  