import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("👋 Hi! Send me anything and I’ll echo it.")

@dp.message()
async def echo(message: Message):
    if message.text:
        await message.answer(message.text)
    else:
        await message.answer("I can only echo text messages 🙂")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
