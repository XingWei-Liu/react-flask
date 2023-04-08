import os
from flask import Flask, render_template, request, jsonify

from src.generate import get_json

os.chdir(os.getcwd())
app = Flask(__name__, template_folder="./template", static_folder="./static/static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/str_test', methods=['POST'])
def str_test():
    str = request.json.get('string').strip()
    str = str + ' test'
    return jsonify({"string": str})

@app.route('/get_png', methods=['GET'])
def get_png():
    json = get_json()
    return json

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
