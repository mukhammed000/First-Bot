import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from bot_classes import Bot, User
from utils import Languages, States

load_dotenv()
token = os.getenv("token")

def main():
    app = ApplicationBuilder().token(token).build()
    user = User("Regular", "English")
    bot = Bot(app, user)
    
    app.add_handler(CommandHandler("start", bot.start)) 
    app.add_handler(CommandHandler("language", bot.language))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()