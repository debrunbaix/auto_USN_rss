import smtplib
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

sendTo = config.get('Mail_Info', 'my_mail')
emailSubject = "Ubuntu News !"

SMTP_SERVER = config.get('Mail_Config', 'SMTP_SERVER')
SMTP_PORT = config.get('Mail_Config', 'SMTP_PORT')
GMAIL_USERNAME = config.get('Mail_Config', 'GMAIL_USERNAME')
GMAIL_PASSWORD = config.get('Mail_Config', 'GMAIL_PASSWORD')
print(GMAIL_PASSWORD)

def sendmail(content):

    #Create Headers
    headers = ["From: " + GMAIL_USERNAME, "Subject: " + emailSubject, "To: " + ", ".join(sendTo),
        "MIME-Version: 1.0", "Content-Type: text/html"]
    headers = "\r\n".join(headers)

    #Connect to Gmail Server
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()

    session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    session.sendmail(GMAIL_USERNAME, sendTo, (headers + "\r\n\r\n" + content).encode('utf-8'))
    session.quit
    print('-- mail send --')