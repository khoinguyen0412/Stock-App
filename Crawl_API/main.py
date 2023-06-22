import new_crawl
import send_mail
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
 
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

@app.route('/send-mail', methods=['POST'])
def compare():
    data = request.get_json()
    curr_list = json.loads(data)
    send_mail.comapre(curr_list)
    return ('', 200)

if __name__ == '__main__':
    app.run(debug=True)
