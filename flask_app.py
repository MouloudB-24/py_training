# Import the Flask class from the flask module
from flask import Flask, jsonify

# Create the instance of the Flask class
app = Flask(__name__)

# Define a route of the root URL
@app.route("/")
def index():
    return {"message": "Hello World!"}