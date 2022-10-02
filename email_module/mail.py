import smtplib

my_email = "madoldsniper@gmail.com"
to_email = "madoldsniper@gmail.com"
user = "madoldsniper@gmail.com"
password = "envqsfsmqwwsmyai"

with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
    # secure the connection(packets sent using ttls)
    connection.ehlo()
    connection.login(user=user, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_email,
        msg="Subject: This is a test subject\n\nTest Message")
