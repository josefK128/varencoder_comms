# smtpclient.py


import smtplib
import email.utils
from email.mime.text import MIMEText
import json


# location of email data-file
filepath = '../db_/lists-028-0116924.json'


# Create the message
with open(filepath, 'r') as f:
    data = json.load(f)
    msg = MIMEText(data['msg'])
    msg['To'] = email.utils.formataddr(('Recipient', data['receivers'][0]))
    msg['From'] = email.utils.formataddr(('Author', data['sender']))
    msg['Subject'] = data['subject']


# send email
server = smtplib.SMTP('127.0.0.1', 1025)
server.set_debuglevel(True) # show communication with the server
try:
    server.sendmail('author@example.com', ['recipient@example.com'], msg.as_string())
finally:
    server.quit()
