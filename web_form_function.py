from flask import Flask, render_template, request
from excel_functions import write_data

app = Flask(__name__)

@app.route('/')
def display_form():
	return render_template("form.html")

@app.route('/', methods=['POST'])
def get_data():
	if request.method == 'POST':
		q1 = request.form['q1']
		q2 = request.form['q2']
		q3 = request.form['q3']
		q4 = request.form['q4']
		q5 = request.form['q5']

	write_data(q1, q2, q3, q4, q5) 
	return render_template("submit_form.html")