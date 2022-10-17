import os
import smtplib
from dotenv import load_dotenv

# load all env variables
load_dotenv()


def send_email():
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        # secure the connection(packets sent using ttls)
        connection.ehlo()
        connection.login(user=os.getenv('user'), password=os.getenv('password'))
        connection.sendmail(
            from_addr=os.environ['my_email'],
            to_addrs=os.environ['my_email'],
            msg="Subject: ISS location Info\n\n Looks Up ☝️🛰the ISS is there in the sky!  Yahoo!")
