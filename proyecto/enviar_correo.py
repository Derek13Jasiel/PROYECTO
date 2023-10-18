from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def enviar(usuario,correo,contra):
    msg = MIMEMultipart()
    message = "contraseña de la cuenta "+ usuario + "   es: "+ contra

    password = "ystr rcps lwxv vxif"
    msg['From'] = "kaorigtshop@gmail.com"
    msg['To'] = correo
    msg['Subject'] = "Recuperacion de Contraseña"
    
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()

    server.login(msg['From'], password)

    server.sendmail(msg['From'], msg['To'], msg.as_string())
