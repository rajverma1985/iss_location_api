import os
import smtplib
from dotenv import load_dotenv

# load all env variables

load_dotenv()

with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
    # secure the connection(packets sent using ttls)
    connection.ehlo()
    connection.login(user=os.getenv('user'), password=os.getenv('password'))
    connection.sendmail(
        from_addr=os.getenv('my_email'),
        to_addrs=os.getenv('my_email'),
        msg="Subject: This is a test subject\n\nTest Message")
