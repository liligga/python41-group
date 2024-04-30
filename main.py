import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
from dotenv import load_dotenv
from os import getenv

load_dotenv()
bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    print(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}")


@dp.message(Command("picture"))
async def send_picture(message: types.Message):
    photo = types.FSInputFile("images/cat.jpg")
    await message.answer_photo(
        photo=photo,
        caption="Котик 🐱"
    )


@dp.message()
async def echo(message: types.Message):
    # print(message)
    await message.answer(message.text)


async def main():

    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
