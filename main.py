from email.message import EmailMessage
import ssl
import smtplib

password = 'yourpasswordtoken'

email_sender = "your@email.com"
email_password = password

email_receiver = "jenic53051@pgobo.com"

subject = "your subject"
body = """
your body texte
"""

em = EmailMessage()
em['from'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())