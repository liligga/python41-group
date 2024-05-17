from aiogram import Router, F, types
from aiogram.filters import Command
from config import database
from pprint import pprint


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
                types.KeyboardButton(text="Хоррор"),
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Книги по жанрам", reply_markup=kb)


book_genres = ("триллер", "хоррор", "фантастика")


@shop_router.message(F.text.lower().in_(book_genres))
async def show_triller(message: types.Message):
    genre = message.text
    print("Пользователь нажал на кнопку", genre)
    data = await database.fetch(
        """SELECT * FROM books 
        INNER JOIN genres ON books.genre_id = genres.id 
        WHERE genres.name = ?""", 
        (genre,)
    )
    pprint(data)
    if not data:
        await message.answer("К сожалению, ничего не нашлось")
        return
    kb = types.ReplyKeyboardRemove()
    await message.answer(f"Книги жанра {genre}:", reply_markup=kb)
    for book in data:
        image = types.FSInputFile(book.get("picture"))
        await message.answer_photo(
            photo=image, 
            caption=f"{book['name']} - {book['author']}\nЦена: {book['price']} сом")
