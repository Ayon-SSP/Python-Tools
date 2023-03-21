
# [https://zetcode.com/python/smtplib/]
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

senderMail,senderPassword = 'exptemptotest@gmail.com','nocdzdqflssnnmra'
receiverMail = 'ayoniiiiii10@gmail.com'


server.starttls()
server.login(senderMail,senderPassword)


clgMails = []
for last3num in range(260,272):
    clgMails.append('200303124'+str(last3num)+'@paruluniversity.ac.in')

# MultiMail
"""

# Faster
server.sendmail(senderMail,clgMails,'One of your classmates, \nWellwisher or a friend.')
# - or -
# slower
# for clgMail in clgMails:
#     server.sendmail(senderMail,clgMail,'You Guys are luckey')
#     print('send mail to',clgMail)
"""


# with subject
from email.mime.text import MIMEText  # Import the email modules we'll need (add subject)
msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'


server.sendmail(senderMail, receiverMail, msg.as_string())