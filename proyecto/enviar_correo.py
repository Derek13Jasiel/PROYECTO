

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
message = "Thank you"

password = "ystr rcps lwxv vxif"
msg['From'] = "kaorigtshop@gmail.com"
msg['To'] = "3062251310311@ingenieria.usac.edu.gt"
msg['Subject'] = "Subscription"
 
msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

server.login(msg['From'], password)

server.sendmail(msg['From'], msg['To'], msg.as_string())

print ("funcion %s:")% (msg['To'])