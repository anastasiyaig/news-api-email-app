import certifi
import smtplib
import ssl
import os


def send_email(composed_message):
    host = "smtp.gmail.com"
    port = 465
    sender_email = 'anastasija.edu1@gmail.com'  # the mailbox u can manage and has access / password to
    sender_password = os.getenv('GMAIL_PASSWORD')  # app password im Gmail Account settings
    email_receiver = 'anastasija.edu1@gmail.com'  # could be any
    context = ssl.create_default_context(cafile=certifi.where())

    # if u want a subject of email as well, use the syntax "Subject: Today's news" before the string content
    composed_email = composed_message
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email_receiver, composed_email)