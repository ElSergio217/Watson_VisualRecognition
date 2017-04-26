from flask import Flask
from watson_developer_cloud import VisualRecognitionV3 as vr
from app import app
from flask import render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		instance = vr(api_key='ea063a17f1589193f1f83656d6608806eee905d0', version='2016-05-20') # API credentials
		img = instance.classify(images_url=request.form['search']) # Identify Image  
		return render_template('result.html', img=img) # Renders template with Image results
	return render_template('index.html')

