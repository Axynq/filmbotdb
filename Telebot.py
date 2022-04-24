import asyncio
from aiogram import Bot, Dispatcher, executor
from Config import TOKEN

bot = Bot(TOKEN, parse_mode="HTMl")
dp = Dispatcher(bot)

if __name__ == "__main__":
    from Handlers import dp
    executor.start_polling(dp)
