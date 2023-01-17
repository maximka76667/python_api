# import requests

# api_url = "https://jsonplaceholder.typicode.com/todos/1"

# response = requests.get(api_url)

# print(response.json())

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return jsonify({"message": "Hello"})


if __name__ == '__main__':
    app.run(debug=True)
