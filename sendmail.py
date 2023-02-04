#sendmail1
#important:
#please substitute fields against * and delete character *

*username = "your username"   
*password = "your password"

from email.mime.multipart import MIMEMultipart
# format email ra bar asas standard tanzim mikonad

from email.mime.text import MIMEText

import smtplib


message = MIMEMultipart()

*message["from"] = "email address sender"
*message["to"] = "email address reciever"
message["subject"] = "send mail from python"
message.attach(MIMEText("Hello from python"))
*with smtplib.SMTP(host="host for your email", port=port) as smtp:
    smtp.ehlo() #hello to smtp
    smtp.starttls() #to encoding
    smtp.login(username, password)
    smtp.send_message(message)
    print("email sent")

