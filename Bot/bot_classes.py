from telegram import Update
from telegram.ext import ContextTypes
from utils import Languages, States, ChoosingLanguage, Greetings
from menu import show_menu, select_language

class Bot:
    def __init__(self, app):
        self.app = app
        self.users = {}
    
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        # Create user if not exists
        if chat_id not in self.users:
            self.users[chat_id] = User(States[0], Languages[0])
        
        await show_menu(update, context, self.users[chat_id])
    
    async def language(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        # Create user if not exists
        if chat_id not in self.users:
            self.users[chat_id] = User(States[0], Languages[0])
            
        await select_language(update, context, self.users[chat_id])
        

class User:
    def __init__(self, state, language):
        self.state = state
        self.language = language
        
    def set_state(self, state):
        self.state = state
    
    def get_state(self): 
        return self.state
    
    def set_language(self, language):
        self.language = language
    
    def get_language(self):
        return self.language