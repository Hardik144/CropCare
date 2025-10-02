import os
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = load_model('model/crop_model.h5')
class_names = ['Apple___Black_rot', 'Apple___Scab', 'Corn___Gray_leaf_spot', 
               'Corn___Healthy', 'Grape___Black_rot', 'Grape___Esca', 
               'Potato___Late_blight', 'Potato___Healthy', 'Tomato___Early_blight', 
               'Tomato___Healthy', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
               'Tomato___Spider_mites', 'Tomato___Target_Spot', 'Tomato___YellowLeafCurlVirus',
               'Tomato___mosaic_virus', 'Rice___Brown_Spot']

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Preprocess the image
        img = load_img(filepath, target_size=(128, 128))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Make prediction
        prediction = model.predict(img_array)
        predicted_index = np.argmax(prediction)
        predicted_class = class_names[predicted_index]
        confidence = round(np.max(prediction) * 100, 2)

        return render_template('index.html', prediction=predicted_class,
                               confidence=confidence, image_path='/' + filepath)

if __name__ == '__main__':
    app.run(debug=True)
