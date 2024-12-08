import os
from twilio.rest import Client
from flask import Flask, request

# Twilio configuration
TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_PHONE_NUMBER = "+18662374849"
USER_PHONE_NUMBER = "4046839747"

# Flask setup
app = Flask(__name__)

# Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms_with_image(image_path):
    # Send an SMS with image and feedback request
    message = client.messages.create(
        body="Visitor detected. Approve or Reject?",
        from_=TWILIO_PHONE_NUMBER,
        to=USER_PHONE_NUMBER,
        media_url=f"http://your_raspberry_pi_ip:5000/static/{image_path}"  # Host image via Flask
    )
    print(f"Message sent: {message.sid}")

@app.route('/sms', methods=['POST'])
def sms_reply():
    # Handle incoming SMS
    incoming_msg = request.form.get('Body').strip().lower()

    if "approve" in incoming_msg:
        print("Visitor Approved")
        # Perform the approve action (e.g., unlock door)
        os.system("python unlock_door_script.py")
    elif "reject" in incoming_msg:
        print("Visitor Rejected")
        # Perform the reject action (e.g., keep door locked)
        os.system("python keep_door_locked_script.py")
    else:
        print("Unrecognized command")
    return "OK", 200

if __name__ == "__main__":
    # Start Flask server for webhooks
    app.run(host='0.0.0.0', port=5000)
