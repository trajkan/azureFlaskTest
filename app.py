
from crypt import methods
from flask import Flask, request, jsonify, render_template, url_for
print('here')
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World'

@app.route('/predict_api', methods=["GET","POST"])
def list_post():
    json_body = request.get_json(force=True)
    predictions = 2 * json_body[0]   
    predictions = list(predictions)
    return jsonify(results = predictions)

@app.route('/testing', methods=["get"])
def test():
    return "Testing api calls"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
