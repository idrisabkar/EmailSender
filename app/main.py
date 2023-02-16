from smtplib import SMTP
from email.message import EmailMessage


email = EmailMessage()
email.set_content("hello wordl!!")
email["From"] = "idrisabkar2018@gmail.com"
email["To"] = "idrissruso@gmail.com"
email["Subject"] = "Test Email"


username = "idrisabkar2018@gmail.com"
password = "mfnesyplsqkuanii"

with SMTP(port=587,host="smtp.gmail.com") as smtp:
    smtp.starttls()
    smtp.login(user=username,password=password)
    smtp.send_message(email)


