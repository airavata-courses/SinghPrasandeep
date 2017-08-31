from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/greeting")
def say_hello():
	return  "Hello Docker from Python!";

if __name__ == '__main__':
    app.run(host='0.0.0.0')
