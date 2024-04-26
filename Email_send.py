import smtplib
import os

email_id = os.environ.get('EMAIL_ADDR')
email_pass = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_id, email_pass)

    subject = 'fight against covid'
    body = 'hey, hi let\'s fight against covid by staying at home'

    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(email_id, 'bomlevaibhav1994@gamil.com', msg)
