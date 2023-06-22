import new_crawl
import send_mail
from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve

 
datas =[]

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return('Welcom to my API')

@app.route('/get-data')
def index():
    data = new_crawl.get_session()
    return jsonify(data)

if __name__ == '__main__':
    serve(app, host="127.0.0.1", port=8080)
