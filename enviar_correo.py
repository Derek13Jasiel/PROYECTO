

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
# create message object instance 
msg = MIMEMultipart()
message = "Thank you"
# setup the parameters of the message 
password = "Hola3Hola3$$adios"
msg['From'] = "derekjasielpatanxocop@gmail.com"
msg['To'] = "3062251310311@ingenieria.usac.edu.gt"
msg['Subject'] = "Subscription"
# add in the message body 
msg.attach(MIMEText(message, 'plain'))
#create server 
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
# Login Credentials for sending the mail 
server.login(msg['From'], password)
# send the message via the server. 
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print ("successfully sent email to %s:")% (msg['To'])