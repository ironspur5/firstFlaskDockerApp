from flask import Flask

app = Flask(__name__)

@app.route('/')
def avengers():
	return 'Avengers'

@app.route('/thor')
def thor():
	return 'Thor'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
