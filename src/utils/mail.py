
from utils.config import Config
import smtplib
from email.mime.text import MIMEText

def send_mail(message):
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    sender=(Config()).cfg['SENDER']
    recipient=(Config()).cfg['RECEIVER']
    mail.login(sender, (Config()).cfg['PASSWORD'])
    msg = MIMEText(message)
    msg['Subject'] = 'Daily results'
    msg['From'] = sender
    msg['To'] = recipient
    mail.send_message(msg)
    mail.close()






