from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

class request(req):

@app.route('/')
def index():
	return req

@app.route('/data')
def data():
	data = {"names":["john", "ddd", "fff", "eee"]}
	return jsonify(data)

if __name__ == '__main__':
	app.run(debug=True, port=8081)



