#!/usr/bin/env python
import smtplib
from email.message import EmailMessage
import ssl

def send_email_route():
    recipient_email = 'rkbillups2@gmail.com'
    print(f'User Input: {recipient_email}')
    
    try:
        send_email(recipient_email)
        return "Email sent successfully!"
    except Exception as e:
        print(f"Failed to send email: {e}")
        return "Failed to send email."

def send_email(email):
    email_sender = 'saintkeyproducts@gmail.com'
    email_password = 'xdlc yogk hhpl apda'
    email_receiver = email

    subject = 'Security Alert: User Detected'
    body = """Hello, this user is at your doorbell"""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 587, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
        raise

def main():
    result = send_email_route()
    print(result)

if __name__ == "__main__":
    main()
