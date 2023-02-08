import requests

response = requests.get("https://todos.json")
data = response.json()

from flask import Flask, request


app = Flask(__name__)


@app.route('/todos/', methods=['GET'])
def get_list():
   if request.method == 'GET':
       data = response.json()
       return data


if __name__ == "__main__":
    app.run()