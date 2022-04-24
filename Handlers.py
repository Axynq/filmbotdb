from Telebot import dp, bot
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery
from aiogram.dispatcher.filters import Command, Text

#Главная клавиатура
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Искать фильм"),
            KeyboardButton(text = "Выбор бота")
        ],
        [
            KeyboardButton(text = "Добавить фильм"),
        ],
    ],
    resize_keyboard = True,
    one_time_keyboard = True
)
#Основная инлайн клавиатура
keyboard = InlineKeyboardMarkup()
keyboard.add(InlineKeyboardButton(text="Жанр", callback_data="genre"))
keyboard.add(InlineKeyboardButton(text="Год", callback_data="year"))
keyboard.add(InlineKeyboardButton(text="Страна", callback_data="country"))

#Клавиатура для добавления фильмов
KeyboardName = InlineKeyboardMarkup()
KeyboardName.add(InlineKeyboardButton(text="Готово", callback_data="done1"))

KeyboardGenre = InlineKeyboardMarkup()
KeyboardGenre.add(InlineKeyboardButton(text="Готово", callback_data="done2"))

KeyboardYear = InlineKeyboardMarkup()
KeyboardYear.add(InlineKeyboardButton(text="Готово", callback_data="done3"))

KeyboardCountry = InlineKeyboardMarkup()
KeyboardCountry.add(InlineKeyboardButton(text="Готово", callback_data="done4"))

keyboardrandom = InlineKeyboardMarkup()
keyboardrandom.add(InlineKeyboardButton(text="Ещё", callback_data="next film"))

@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    await message.answer("Алоха, значит фильмец посмотреть захотелось?\nЧто б узнать о возможностях пропиши /help", reply_markup=menu)

@dp.message_handler(commands=['help'])
async def process_help_command(message: Message):
    await message.answer("Команды:\n1. Бот - вызов меню\n2. Бот закинет фильмец, котрый он смотрел и ему понравилось.")

@dp.message_handler(text = "Бот")
async def show_menu(message: Message):
    await message.answer("Что вы хотите сделать?",
reply_markup = menu)

@dp.message_handler(text="Искать фильм")
async def find_film(message: Message):
    await message.answer("По какому критерию будем искать?",
reply_markup = keyboard)

@dp.message_handler(text = "Добавить фильм")
async def show_menu(message: Message):
    await message.answer("Напишите название фильма, после чего нажмите на кнопку",
reply_markup = KeyboardName)

@dp.callback_query_handler(text="done1")
async def send_random_value(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer("Теперь жанр",reply_markup = KeyboardGenre)
        await call.answer()

@dp.callback_query_handler(text="done2")
async def send_random_value(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer("Год",reply_markup = KeyboardYear)
        await call.answer()

@dp.callback_query_handler(text="done3")
async def send_random_value(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer("Ну и наконец страну",reply_markup = KeyboardCountry)
        await call.answer()

@dp.callback_query_handler(text="done4")
async def send_random_value(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer("Готово, спасибо за пополнение базы, цём")
        await call.answer()

@dp.message_handler(text="Выбор бота")
async def find_film(message: Message):
    await message.answer("Тут будет случайный фильм",
reply_markup = keyboardrandom)
