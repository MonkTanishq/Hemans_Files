import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename



app = Flask(__name__)




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods = ['GET', 'POST'])
def detect():
	if request.method == 'POST':
		file = request.files['inpFile']
		filename = secure_filename(file.filename)
		file.save(os.path.join('uploads', filename))
		return redirect(url_for('prediction', filename=filename))
	return render_template("index.html", data = file)
	
	
@app.route('/prediction/<filename>')
def prediction(filename):
	my_image = plt.imread(os.path.join('uploads', filename))
	my_image_re = resize(my_image, (32,32,3))
	with graph.as_default():
		set_session(sess)
		probabilities = model.predict(np.array( [my_image_re,] ))[0,:]
		print(probabilities)
		number_to_class = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
		index = np.argsort(probabilities)
		predictions = {
		"class1":number_to_class[index[9]],
		"class2":number_to_class[index[8]],
		"class3":number_to_class[index[7]],
		"prob1":probabilities[index[9]],
		"prob2":probabilities[index[8]],
		"prob3":probabilities[index[7]],
		}
	return render_template('predict.html', predictions=predictions)

if __name__ == "__main__":
    app.run(debug=True)
