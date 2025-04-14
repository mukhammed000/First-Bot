from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from utils import Languages, States, ChoosingLanguage, MenuButtons, Greetings

async def select_language(update: Update, context: ContextTypes.DEFAULT_TYPE, user):
    user_language = user.get_language()
    text = ""
    
    if user_language == "English":
        text = ChoosingLanguage[0]
    elif user_language == "Russian":
        text = ChoosingLanguage[1]
    elif user_language == "Uzbek":
        text = ChoosingLanguage[2]
    else:
        text = "\n".join(ChoosingLanguage[:3])
    
    keyboards = [[KeyboardButton(lang) for lang in Languages]] 
    reply_keyboard = ReplyKeyboardMarkup(keyboards, resize_keyboard=True)
    
    await update.message.reply_text(text, reply_markup=reply_keyboard) 

async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, user):
    user_language = user.get_language() 
    keyboards = []
    
    if user_language == "English":
        keyboards = [
            [KeyboardButton(MenuButtons[0][0]), KeyboardButton(MenuButtons[0][1])],
            [KeyboardButton(MenuButtons[0][2]), KeyboardButton(MenuButtons[0][3])],
            [KeyboardButton(MenuButtons[0][4])] 
        ]
    elif user_language == "Russian":
        keyboards = [
            [KeyboardButton(MenuButtons[1][0]), KeyboardButton(MenuButtons[1][1])],
            [KeyboardButton(MenuButtons[1][2]), KeyboardButton(MenuButtons[1][3])],
            [KeyboardButton(MenuButtons[1][4])] 
        ]
    elif user_language == "Uzbek":
        keyboards = [
            [KeyboardButton(MenuButtons[2][0]), KeyboardButton(MenuButtons[2][1])],
            [KeyboardButton(MenuButtons[2][2]), KeyboardButton(MenuButtons[2][3])],
            [KeyboardButton(MenuButtons[2][4])] 
        ]
    else:
        keyboards = [
            [KeyboardButton(MenuButtons[0][0]), KeyboardButton(MenuButtons[0][1])],
            [KeyboardButton(MenuButtons[0][2]), KeyboardButton(MenuButtons[0][3])],
            [KeyboardButton(MenuButtons[0][4])] 
        ]
    
    reply_keyboard = ReplyKeyboardMarkup(keyboards, resize_keyboard=True) 
    
    await update.message.reply_text("Menu", reply_markup=reply_keyboard) 