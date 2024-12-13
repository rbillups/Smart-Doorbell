
import time
import os
#import telebot  # Import the correct module
#from telegram import Update
from telegram.ext import Update

#Bot,st
from telegram.ext import Application, MessageHandler, filters, ContextTypes, Update

async def echo(update: Update,context: ContextTypes.DEFAULT_TYPE):
    user_message= update.message.text
    await update.message.reply_text(f"You said: {user_message}")

def testing_main():
    # print("Button pressed")
    # #image_path = "/home/keybillups/Smart-Doorbell/Smartfolder/my_project/static/visitor.jpg"
    # image_path= "/Users/keybillups/Documents/Smart-Doorbell"
    # #os.system(f"libcamera-still -o {image_path}")
    # print(f"Image saved at {image_path}")

    # # Handle button press and send image via telegram bot
    # telebot.handle_button_press(image_path)

    # # This will run the bot without needing asyncio.run()
    # telebot.initializeBot()
    BOT_TOKEN = "7763295015:AAHLM4cjlQsVxkn7GqqR-tTJ6RJDhAeFFcs"
    CHAT_ID = "5820351650"

    app= Application.builder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Run the main code
if __name__ == '__main__':
    # import asyncio
    # asyncio.run(testing_main())  # You don't need to call asyncio.run() in the bot file anymore
    testing_main()
