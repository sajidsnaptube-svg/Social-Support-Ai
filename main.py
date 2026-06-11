import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio
import google.generativeai as genai

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("👋 Send me a photo and I will generate caption + hashtags!")

@dp.message()
async def handle(message: Message):
    if message.photo:
        prompt = """
Generate SEO caption, viral caption, 20 hashtags and CTA.
Language: Bangla + English mix.
"""

        result = model.generate_content(prompt)
        await message.answer(result.text)
    else:
        await message.answer("Please send a photo 📸")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
