import new_crawl
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_apscheduler import APScheduler
from waitress import serve
import requests
from email.message import EmailMessage
import ssl 
import smtplib
import mysql.connector
import os
import json
from dotenv import load_dotenv


load_dotenv()
email_sender = os.getenv('MAIL_FROM_ADDRESS')
email_password = os.getenv('MAIL_PASSWORD')
my_port = os.getenv('PORT')

app = Flask(__name__)
CORS(app)
sched = APScheduler()

@app.route('/')
def home():
    return('Welcom to my API')

@app.route('/get-data')
def index():
    data = new_crawl.get_session()
    return jsonify(data)

# ---------------------------------------------------------------------------------

def send_mail():
    print('This is called')
    r = requests.get(f'http://127.0.0.1:{my_port}/get-data')
    current_list = json.loads(r.text)
    mydb = mysql.connector.connect(
    host= os.getenv('DB_HOST'),
    user=os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_DATABASE'),
    )

    mycursor = mydb.cursor(buffered=True)
    
    sender_info = []

    for item in current_list:
        curr_code = item["stock_code"]
        curr_price = float(item["current_price"])
        sql = f'SELECT email,user_price,stock_code FROM users WHERE stock_code="{curr_code}" AND user_price="{curr_price}" AND is_active=1'
        mycursor.execute(sql)
        for x in mycursor:
            sender_info.append(x)

    if sender_info:
        for user in sender_info:
            email = user[0]
            user_price = user[1]
            stock_code = user[2]
            sql = 'UPDATE users SET is_active=FALSE WHERE email = %s AND user_price = %s AND stock_code = %s'
            val = (email,user_price,stock_code)
            mycursor.execute(sql,val)
            mydb.commit()

            email_receiver = f"{email}"
            stock_send = f"{stock_code}"
            subject = f"{stock_code}'S PRICE MEETS YOUR EXPECTATION !!!"

            body = f"""
    Hello, 
    From the live update of the stock price, the price of the {stock_send} is currently {user_price}. The price meets your expectation.
            """

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            context  = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver,em.as_string())

    else:
        return None
    
    mydb.close()

if __name__ == '__main__':
    sched.add_job(id = "Send-mail", func=send_mail, trigger = 'interval', seconds = 60)
    sched.start()
    serve(app, host="127.0.0.1", port=my_port)
