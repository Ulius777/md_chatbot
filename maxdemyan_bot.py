import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Ініціалізація бота
API_TOKEN = os.getenv("BOT_API_TOKEN")
GPT_API_KEY = os.getenv("OPENAI_API_KEY")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Привіт! Я MaxDemyan бот. Напиши щось, і я відповім.")

@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(f"Ти написав: {message.text}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

