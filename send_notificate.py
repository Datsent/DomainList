import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
def send_email(domain, days):

    username = "****@mail.com"
    password = "*****"
    mail_from = "****@mail.com"
    mail_to = "****@mail.com"
    mail_subject = f"Need to renew {domain}"
    mail_body = f'''Hello
You need to renew {domain}, left only {days} days.
Thank you 
'''

    mimemsg = MIMEMultipart()
    mimemsg['From']=mail_from
    mimemsg['To']=mail_to
    mimemsg['Subject']=mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))
    connection = smtplib.SMTP(host='smtp.office365.com', port=587)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mimemsg)
    connection.quit()

if __name__ == '__main__':
    send_email('1102.co.il', 23)