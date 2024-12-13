from telegram import Update  
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler  
import RPi.GPIO as GPIO  
import os  
import time  
  
# Define the BOT_TOKEN and CHAT_ID variables  
BOT_TOKEN = "17768295015:AAHLMA0j1QsVxkn7GqgR-ETJSRJ0hAeFFC"  
CHAT_ID = "-1001234567890"  
  
# Define the button pins  
buttonPin = 17  
buttonPina = 23  
  
# Define the bot  
application = Application.builder().token(BOT_TOKEN).build()  
  
# Define the echo function  
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):  
   user_response = update.message.text  
   user_response = user_response.upper()  
   print(f"User response: {user_response}")  
  
   if user_response == "APPROVE":  
      await update.message.reply_text("Image approved!")  
   elif user_response == "DENY":  
      await update.message.reply_text("Image denied!")  
   else:  
      await update.message.reply_text("Invalid response, please reply with APPROVE or DENY.")  
  
# Define the start function  
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):  
   await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello!")  
  
# Define the handle_button_press function  
async def handle_button_press(image_path):  
   await application.bot.send_message(chat_id=CHAT_ID, text="Button pressed! Here's the image:")  
   with open(image_path, "rb") as image:  
      await application.bot.send_photo(chat_id=CHAT_ID, photo=image)  
   await application.bot.send_message(chat_id=CHAT_ID, text="Reply with APPROVE or DENY.")  
  
# Define the testing main function  
async def testing_main():  
   print("Testing main function")  
   image_path = "/home/pi/project/visitor.jpg"  
   os.system(f"raspistill -o {image_path}")  
   print(f"Image saved at {image_path}")  
   await handle_button_press(image_path)  
  
   # Add the echo and start handlers  
   start_handler = CommandHandler("start", start)  
   application.add_handler(start_handler)  
   application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))  
  
   # Run the application  
   await application.run_polling()  
  
# Run the testing main function  
import asyncio  
asyncio.run(testing_main())
