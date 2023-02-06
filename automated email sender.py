#AUTOMATED EMAIL SENDER

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to, subject, message):
    msg = MIMEMultipart()
    msg['From'] = "youremail@example.com"
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("youremail@example.com", "yourpassword")
        server.sendmail("youremail@example.com", to, msg.as_string())
        server.close()

        print("Email sent successfully!")
    except Exception as e:
        print("Something went wrong: " + str(e))

to = "recipientemail@example.com"
subject = "Test email from Python"
message = "This is a test email sent from Python."
send_email(to, subject, message)
