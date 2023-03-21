"""

Mail:
    1. Sending to a persin
    2. Sending to a group of people
    3. Sending to a group of people with a file
    4. Sending to a group of people with a file and a message
    5. Sending to a group of people with a file and a message and a subject
    6. 
"""



import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587) 

clgMails = ['200303124271@paruluniversity.ac.in']

senderMail,senderPassword = 'exptemptotest@gmail.com','nocdzdqflssnnmra'
receiverMail = 'ayoniiiiii10@gmail.com'


server.starttls()
server.login(senderMail,senderPassword)
for clgMail in clgMails:
    server.sendmail(senderMail,clgMail,'Test was sucessfull')
print('send mail')



#  for sub title
"""
import smtplib
from email.message import EmailMessage



msg = EmailMessage()
msg.set_content('This is my message')

msg['Subject'] = 'This is the sub titles'
msg['From'] = "me@gmail.com"
msg['To'] = '200303124271@paruluniversity.ac.in'

# Send the message via our own SMTP server.
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('exptemptotest@gmail.com', 'nocdzdqflssnnmra')
server.send_message(msg)
server.quit()


"""