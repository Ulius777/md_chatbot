
import logging
import openai
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_webhook

# Токени
API_TOKEN = '7579854487:AAG5lzBiX7gq9N7qaW15x6QI-A_5uB_T9Z4'
GPT_API_KEY = os.getenv("OPENAI_API_KEY")  # Встановити окремо

# Константи вебхука
WEBHOOK_HOST = 'https://your-app-name.onrender.com'  # Замінити на свій хост
WEBHOOK_PATH = f'/webhook/{API_TOKEN}'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT', 8000))

# Ініціалізація
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# GPT функція
openai.api_key = GPT_API_KEY

def build_prompt(user_input):
    return f"Ти — Макс Демʼян. Відповідай глибоко, по-філософськи, з іронією. Запит: {user_input}"

async def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Ти глибокий, іронічний мислитель, який відповідає від імені Макса Демʼяна."},
                  {"role": "user", "content": prompt}],
        max_tokens=800,
        temperature=0.85
    )
    return response['choices'][0]['message']['content']

@dp.message_handler()
async def handle_message(message: types.Message):
    prompt = build_prompt(message.text)
    answer = await ask_gpt(prompt)
    await message.answer(answer)

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    logging.warning('Bye!')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
# redeploy test
