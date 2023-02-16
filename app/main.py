from smtplib import SMTP
from email.message import EmailMessage


email = EmailMessage()
email.set_content("hello wordl!!")
email["From"] = "*************"
email["To"] = "*************"
email["Subject"] = "Test Email"


username = "*****************"
password = "******************"

with SMTP(port=587,host="smtp.gmail.com") as smtp:
    smtp.starttls()
    smtp.login(user=username,password=password)
    smtp.send_message(email)


