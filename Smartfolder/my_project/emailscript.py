#!/usr/bin/env python
import smtplib
from email.message import EmailMessage
import ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

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
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'saintkeyproducts@gmail.com'
    smtp_password = 'iche mpdv ztvr tveb'
    current_dir = os.getcwd()
    image_path = os.path.join(current_dir, 'nks.jpg')
    
    # Print the current directory and image path
    print(f'Current Directory: {current_dir}')
    print(f'Image Path: {image_path}')

    subject = 'Security Alert: User Detected'
    body = """Hello, this user is at your doorbell"""

    user_message = MIMEText(body)
    user_message['Subject'] =     subject 
    user_message['From'] = smtp_username
    user_message['To'] = 'jboogie0123@gmail.com'

    print("in email"+ user_message.as_string())

    # Attach the image
    with open(image_path, 'rb') as img:
        img_data = img.read()
        img_name = image_path.split('/')[-1]
        user_message.add_attachment(img_data, maintype='image', subtype='jpeg', filename=img_name)

    context = ssl.create_default_context()

    try:
        # Establish a connection to the SMTP server
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.ehlo()
        smtp_connection.starttls()
        smtp_connection.ehlo()
        smtp_connection.login(smtp_username, smtp_password)

        # Send the emails
        smtp_connection.sendmail(smtp_username, 'jboogie0123@gmail.com', user_message.as_string())
        smtp_connection.quit()
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
        raise
    
    print("Emails sent successfully")


def main():
    result = send_email_route()
    print(result)

if __name__ == "__main__":
    main()
