# python3 -m flask run
# ctrl+c

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"