from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from database.database import Database
from pathlib import Path


load_dotenv()
database = Database(Path('__file__').parent / 'db.sqlite')

dev = getenv("DEV", 0)
if not dev:
    from aiogram.client.session.aiohttp import AioHTTPSession

    print("started on serve")
    session = AioHTTPSession(proxy=getenv("PROXY"))
    bot = Bot(token=getenv("TOKEN"), session=session)

else:
    print("started on dev")
    bot = Bot(token=getenv("TOKEN"))

dp = Dispatcher()


async def set_menu():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="picture", description="Картинка"),
        types.BotCommand(command="opros", description="Пройдите опрос"),
        types.BotCommand(command="shop", description="Магазин")
    ])