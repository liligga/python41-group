import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
from dotenv import load_dotenv
from os import getenv

from handlers.picture import picture_router


load_dotenv()
bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher()


# обработчики
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    print(message.from_user)
    # await message.answer(f"Привет, {message.from_user.first_name}")
    await message.reply(f"Привет, {message.from_user.first_name}")

# @dp.message()
# async def echo(message: types.Message):
#     # print(message)
#     await message.answer(message.text)

async def main():
    # регистрация обработчиков
    dp.include_router(picture_router)
    # запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())