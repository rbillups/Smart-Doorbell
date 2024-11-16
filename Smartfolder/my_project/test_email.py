#!/usr/bin/env python
import smtplib
from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText
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
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    subject = 'Security Alert: User Detected'
    body = """Hello, this user is at your doorbell"""

    user_message = MIMEText(body)
    user_message['Subject'] =     subject 
    user_message['From'] = email_sender
    user_message['To'] = 'jboogie0123@gmail.com'

    print("in email"+ user_message.as_string())

    # Establish a connection to the SMTP server
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.ehlo()
    smtp_connection.starttls()
    smtp_connection.ehlo()
    smtp_connection.login(email_sender, email_password)

    # Send the emails
    smtp_connection.sendmail(email_sender, 'jboogie0123@gmail.com', user_message.as_string())
    smtp_connection.quit()

    context = ssl.create_default_context()

    # try:
    #     smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    #     smtp_connection.ehlo()
    #     smtp_connection.starttls()
    #     smtp_connection.ehlo()
    #     smtp_connection.login(email_sender, email_password)

    #     # Send the emails
    #     smtp_connection.sendmail(email_sender, 'rkbillups2@gmail.com', user_message.as_string())
    #     smtp_connection.quit()
    # except smtplib.SMTPException as e:
    #     print(f"SMTP error occurred: {e}")
    #     raise

def main():
    result = send_email_route()
    print(result)

if __name__ == "__main__":
    main()
