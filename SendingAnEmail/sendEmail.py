import smtplib
from email.mime.text import MIMEText

smtp_server = 'smtp.gmail.com'
smtp_port = 587    # For TLS
sender_email = 'your sender Email'
receiver_email = 'your receiver Email'
message = 'Hello, this is a practice for sending emails via Python'

msg = MIMEText(message)
msg['Subject'] = 'Automated Email'
msg['From'] = sender_email
msg['To'] = receiver_email

# Setup the Connection to the SMTP Server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # For Encryption

    # Login to your Gmail account
    password = input("Enter your Gmail password and press enter: ")
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, [receiver_email], msg.as_string())

