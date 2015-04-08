from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib

#password = raw_input("pass: ")
msg = MIMEMultipart()
msg.attach(MIMEImage(file("aritro.png").read()))


mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('aritropat@gmail.com', "!Aaritrop23")

mail.sendmail('aritropat@gmail.com', 'souravsen1990@gmail.com', msg.as_string())

mail.close()
