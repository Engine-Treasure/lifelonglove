#!/usr/bin/python

import os
import smtplib
from email.mime.text import MIMEText


# password = os.getenv("EMAIL_PASSWORD_163")
password = os.getenv("EMAIL_PASSWORD_QQ")


server = smtplib.SMTP("smtp.kissg.org", port=465)


def send_email(sender="blessing@kissg.org", recipient="me@kissg.org",
        subject="Mission Complete", body="Mission Complete"):

    msg = MIMEText(body)

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient


    server.login(msg["From"], password)

    try:
        server.sendmail(msg["From"], [msg["To"]], msg.as_string())
    except Exception as e:
        print(e.message)
        return False
    else:
        print("A")
        return True
    finally:
        server.quit()

if __name__ == "__main__":
    send_email(recipient="13587509571@139.com")
