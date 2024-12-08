from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters

BOT_TOKEN = "your_token_here"
CHAT_ID = "your_chat_id_here"

bot = Bot(token=BOT_TOKEN)

def handle_button_press(image_path):
    bot.send_message(chat_id=CHAT_ID, text="Button pressed! Here's the image:")
    with open(image_path, 'rb') as img:
        bot.send_photo(chat_id=CHAT_ID, photo=img)
    bot.send_message(chat_id=CHAT_ID, text="Reply with APPROVE or DENY.")

def handle_response(update, context):
    user_response = update.message.text.strip().upper()
    if user_response == "APPROVE":
        bot.send_message(chat_id=CHAT_ID, text="Image approved!")
    elif user_response == "DENY":
        bot.send_message(chat_id=CHAT_ID, text="Image denied!")
    else:
        bot.send_message(chat_id=CHAT_ID, text="Invalid response. Please reply with APPROVE or DENY.")

def initializeBot():
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_response))
    updater.start_polling()
