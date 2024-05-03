from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv


load_dotenv()
bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher()


async def set_menu():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="picture", description="Картинка")
    ])