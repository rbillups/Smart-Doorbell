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

    admin_message = MIMEText('Someone is at your doorbell')
    admin_message['Subject'] = 'Security Alert: User Detected'
    admin_message['From'] = smtp_username
    admin_message['To'] = 'rkbillups2@gmail.com'

    # Attach the image
    with open(image_path, 'rb') as img:
        img_data = img.read()
        img_name = image_path.split('/')[-1]
        admin_message.add_attachment(img_data, maintype='image', subtype='jpeg', filename=img_name)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls(context=context)
            smtp.ehlo()
            smtp.login(smtp_username, smtp_password)
            smtp.sendmail(smtp_username, 'rkbillups2@gmail.com', admin_message.as_string())
            smtp.quit()
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
        raise
    
    print("Emails sent successfully")


def main():
    result = send_email_route()
    print(result)

if __name__ == "__main__":
    main()
