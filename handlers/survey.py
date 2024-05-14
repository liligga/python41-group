from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import database


survey_router = Router()


# FSM - Finite State Machine - конечный автомат
class BookSurvey(StatesGroup):
    name = State() # name - имя пользователя
    age = State() # age - возраст пользователя
    gender = State() # gender - пол пользователя
    genre = State() # genre - любимый жанр литературы
    rating = State()


@survey_router.message(Command("opros"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.name)
    await message.answer("Как вас зовут?")

@survey_router.message(BookSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    # await message.answer(f"Спасибо, {name}!")
    await state.update_data(name=name) # обновляем данные {name: "Igor"}
    await state.set_state(BookSurvey.age)
    await message.answer("Сколько вам лет?")

@survey_router.message(BookSurvey.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Пожалуйста, введите число")
        return
    age = int(age)
    if age < 10 or age > 100:
        await message.answer("Пожалуйста, введите возраст от 10 до 100")
        return
    await state.update_data(age=age) # {name: "Igor", age: 18}
    await state.set_state(BookSurvey.gender)
    await message.answer("Ваш пол?")

@survey_router.message(BookSurvey.gender)
async def process_gender(message: types.Message, state: FSMContext):
    gender = message.text
    await state.update_data(gender=gender)
    await state.set_state(BookSurvey.genre)
    await message.answer("Ваш любимый жанр литературы?")

@survey_router.message(BookSurvey.genre)
async def process_genre(message: types.Message, state: FSMContext):
    genre = message.text
    await state.update_data(genre=genre)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="отлично")],
            [types.KeyboardButton(text="хорошо")],
            [types.KeyboardButton(text="плохо")]
        ],
        resize_keyboard=True
    )
    await state.set_state(BookSurvey.rating)
    await message.answer("Поставьте нам рейтинг:", reply_markup=kb)

ratings = ["плохо", "хорошо", "отлично"]

@survey_router.message(BookSurvey.rating, F.text.lower().in_(ratings))
async def process_rating(message: types.Message, state: FSMContext):
    rating = message.text
    rating = ratings.index(rating) + 3
    await state.update_data(rating=rating)
    await message.answer(f"Спасибо за прохождение опроса, {message.from_user.full_name}!")
    data = await state.get_data()
    print(data)
    await database.execute(
        "INSERT INTO surveys (name, age, gender, genre, rating) VALUES (?, ?, ?, ?, ?)",
        (data["name"], data["age"], data["gender"], data["genre"], data["rating"]),
    )
    await state.clear()