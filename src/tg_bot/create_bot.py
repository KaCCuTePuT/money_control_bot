from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config.settings import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
