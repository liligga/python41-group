from aiogram import Router, F, types
from aiogram.filters import Command


shop_router = Router()


@shop_router.message(Command("shop"))
async def show_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Фантастика"),
                types.KeyboardButton(text="Триллер")
            ],
            [
                types.KeyboardButton(text="Художественная литература"),
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Книги по жанрам", reply_markup=kb)


@shop_router.message(F.text.lower() == "триллер")
async def show_triller(message: types.Message):
    await message.answer("Книги жанра Триллер")


@shop_router.message(F.text.lower() == "Фантастика")
async def show_triller(message: types.Message):
    await message.answer("Книги жанра Триллер")