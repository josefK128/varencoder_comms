# gmail.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = '''Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You
'''
#The mail addresses and password
sender_address = 'mark.rudolph@gmail.com'
sender_pass = 'xxxxxxx'
receiver_address = 'mark.rudolph@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')




#=> Traceback (most recent call last):
#=>   File "gmail.py", line 24, in <module>
#=>     session.login(sender_address, sender_pass) #login with mail_id and password
#=>   File "C:\Users\mark_\AppData\Local\Programs\Python\Python38-32\lib\smtplib.py", line 734, in login
#=>     raise last_exception
#=>   File "C:\Users\mark_\AppData\Local\Programs\Python\Python38-32\lib\smtplib.py", line 723, in login
#=>     (code, resp) = self.auth(
#=>   File "C:\Users\mark_\AppData\Local\Programs\Python\Python38-32\lib\smtplib.py", line 646, in auth
#=>     raise SMTPAuthenticationError(code, resp)
#=> smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials b15sm5397501pjb.18 - gsmtp')
