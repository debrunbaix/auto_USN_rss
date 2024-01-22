import smtplib
import configparser
from time import strftime, localtime

config = configparser.ConfigParser()
config.read('config.ini')

sendTo = (config.get('Mail_Info', 'my_mail')).split(',')
emailSubject = "Ubuntu News !"

SMTP_SERVER = config.get('Mail_Config', 'SMTP_SERVER')
SMTP_PORT = config.get('Mail_Config', 'SMTP_PORT')
GMAIL_USERNAME = config.get('Mail_Config', 'GMAIL_USERNAME')
GMAIL_PASSWORD = config.get('Mail_Config', 'GMAIL_PASSWORD')

def sendmail(content):

    #Create Headers
    headers = ["From: " + GMAIL_USERNAME, "Subject: " + emailSubject, "To: " + ", ".join(sendTo),
        "MIME-Version: 1.0", "Content-Type: text/html"]
    headers = "\r\n".join(headers)

    # Connect to Gmail Server
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()
# 
    session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    session.sendmail(GMAIL_USERNAME, sendTo, (headers + "\r\n\r\n" + content).encode('utf-8'))
    session.quit
# 
    time_string = strftime("%m/%d/%Y, %H:%M:%S", localtime())
    print('Mail send at : ' + time_string)
    with open('log.txt', 'a') as file_to_write:
        file_to_write.write(f'Mail send at : {time_string} to : {sendTo}' + '\n')