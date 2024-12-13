from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler
import RPi.GPIO as GPIO
import os
import time
import asyncio
from typing import Optional

class DoorBellBot:
    def __init__(self, token: str, chat_id: str, button_pins: list[int]):
        # Initialize bot configuration
        self.token = token
        self.chat_id = chat_id
        self.button_pins = button_pins
        self.application: Optional[Application] = None
        
        # Setup GPIO
        GPIO.setmode(GPIO.BCM)
        for pin in button_pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pin, GPIO.FALLING, 
                                callback=self._button_callback,
                                bouncetime=2000)

    def _button_callback(self, channel):
        # Create event loop if it doesn't exist
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        
        loop.create_task(self._handle_button_press())

    async def _handle_button_press(self):
        try:
            image_path = "/home/pi/project/visitor.jpg"
            os.system(f"raspistill -o {image_path}")
            print(f"Image captured at {image_path}")
            
            if self.application and self.application.is_running:
                await self.application.bot.send_message(
                    chat_id=self.chat_id, 
                    text="Button pressed! Here's the image:"
                )
                
                with open(image_path, "rb") as image:
                    await self.application.bot.send_photo(
                        chat_id=self.chat_id,
                        photo=image
                    )
                await self.application.bot.send_message(
                    chat_id=self.chat_id,
                    text="Reply with APPROVE or DENY."
                )
        except Exception as e:
            print(f"Error handling button press: {e}")

    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            user_response = update.message.text.upper()
            print(f"User response: {user_response}")

            if user_response == "APPROVE":
                await update.message.reply_text("✅ Image approved!")
            elif user_response == "DENY":
                await update.message.reply_text("❌ Image denied!")
            else:
                await update.message.reply_text(
                    "Invalid response, please reply with APPROVE or DENY."
                )
        except Exception as e:
            print(f"Error in echo handler: {e}")

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="👋 Hello! I'm your doorbell bot. I'll send you images when someone rings!"
        )

    async def setup(self):
        # Initialize application
        self.application = Application.builder().token(self.token).build()

        # Add handlers
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo)
        )

        # Initialize the application
        await self.application.initialize()

    async def run(self):
        try:
            # Setup the application
            await self.setup()

            print("Bot started! Press Ctrl+C to stop.")
            await self.application.run_polling(close_loop=False)

        except Exception as e:
            print(f"Error running bot: {e}")
        finally:
            if self.application:
                await self.application.shutdown()
            GPIO.cleanup()

async def main():
    # Configuration
    BOT_TOKEN = "17768295015:AAHLMA0j1QsVxkn7GqgR-ETJSRJ0hAeFFC"
    CHAT_ID = "-1001234567890"
    BUTTON_PINS = [17, 23]

    # Initialize and run bot
    bot = DoorBellBot(BOT_TOKEN, CHAT_ID, BUTTON_PINS)
    await bot.run()

if __name__ == "__main__":
    asyncio.run(main())