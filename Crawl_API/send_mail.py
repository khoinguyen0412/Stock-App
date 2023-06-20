from email.message import EmailMessage
import ssl 
import smtplib
import mysql.connector 


email_sender = "nguyenkhoi2227@gmail.com"
email_password = "suxu qyqp dsix mnqr"


def comapre(current_list):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="stockdb"
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
            sql = f'UPDATE users SET is_active=0 WHERE email = %s AND user_price = %s AND stock_code = %s'
            val = (f"{email}",f"{user_price}",f"{stock_code}")
            mycursor.execute(sql,val)

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
       




    