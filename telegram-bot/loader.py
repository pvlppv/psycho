from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_SQLite.db import Database

db = Database('/Users/pavelpopov/PycharmProjects/TelegramBotTemplate/db.db')
# db = Database('/root/bot/db.db')

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

__all__ = ['bot', 'storage', 'dp', 'db']
