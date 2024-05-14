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
                types.KeyboardButton(text="хоррор"),
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Книги по жанрам", reply_markup=kb)


book_genres = ("триллер", "хоррор", "фантастика")


@shop_router.message(F.text.lower().in_(book_genres))
async def show_triller(message: types.Message):
    genre = message.text
    kb = types.ReplyKeyboardRemove()
    await message.answer(f"Книги жанра {genre}", reply_markup=kb)
