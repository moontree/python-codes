#  coding:utf-8
import smtplib
from email.mime.text import MIMEText
import base64
import time
import hashlib

def send_mail(to_addr, content):
    smtp_host = 'smtp.host' # address of smtp server
    from_addr = 'username@mail.com' # your email address
    username = 'username'
    password = 'password'
    subject = 'subject'
    # 初始化邮件
    mail = MIMEText(content , 'plain', 'utf-8')
    mail['Subject'] = subject
    mail['From'] = from_addr
    mail['To'] = to_addr

    try:
        smtp = smtplib.SMTP(smtp_host)
        smtp.set_debuglevel(False)
        smtp.ehlo()
        # if use tls
	# smtp.starttls()
        # smtp.ehlo()
        smtp.login(username, password)

        smtp.sendmail(from_addr, to_addr, mail.as_string())
        smtp.close()
        print 'OK'
    except Exception as e:
        print e
