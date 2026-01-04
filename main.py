import os
import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

# ===== Load token =====
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set")

# ===== Bot setup =====
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("👋 Hi! Send me anything and I’ll echo it.")

@dp.message()
async def echo(message: Message):
    if message.text:
        await message.answer(message.text)

# ===== Web server =====
async def ping(request):
    return web.json_response({
        "status": "ok",
        "message": "Bot is running 🚀"
    })

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", ping)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "0.0.0.0", 8000)
    await site.start()

    print("🌐 Web server running on http://0.0.0.0:8000")

# ===== Main =====
async def main():
    print("🤖 Bot is running...")
    await asyncio.gather(
        dp.start_polling(bot),
        start_web_server()
    )

if __name__ == "__main__":
    asyncio.run(main())
