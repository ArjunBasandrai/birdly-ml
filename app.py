
from flask import Flask, render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
import os
import numpy as np
import tensorflow as tf

class_names = ['Asian Green Bee-Eater','Brown-Headed Barbet','Cattle Egret','Common Kingfisher','Common Myna','Common Rosefinch','Common Tailorbird','Coppersmith Barbet','Forest Wagtail','Gray Wagtail','Hoopoe','House Crow','Indian Grey Hornbill','Indian Peacock','Indian Pitta','Indian Roller','Jungle Babbler','Northern Lapwing','Red-Wattled Lapwing','Ruddy Shelduck','Rufous Treepie','Sarus Crane','White Wagtail','White-Breasted Kingfisher','White-Breasted Waterhen']
model = tf.keras.models.load_model("model/model.h5")

app = Flask(__name__)
app.secret_key="t34s"
app.config['UPLOAD_FOLDER'] = os.path.join('static','uploads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit_file():
	if request.method == 'POST':
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file:
			filename = secure_filename(file.filename)
			file.save(os.path.join("static/uploads/",filename))
			image = tf.keras.utils.load_img('static/uploads/'+filename, target_size=(224, 224))
			input_arr = tf.keras.utils.img_to_array(image)
			input_arr = np.array([input_arr])
			input_arr = tf.image.resize(input_arr,(224,224))
			predictions = model.predict(input_arr,verbose=0)
			score = tf.nn.softmax(predictions[0])
			predicted_class = class_names[np.argmax(predictions)]
			label, acc = predicted_class, float(100*np.max(score))
			flash(label)
			flash("{:.2f}".format(acc))
			flash(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect('/')


if __name__ == "__main__":
    app.run()